import random


colors = ['♠', '♣', '♦', '♥']

signs = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']


class Deck:

    def __init__(self):
        """
           Initialise le Deck en créant les 52 cartes
        """
        self.cards = []
        for i in signs:
            for j in colors:
                card = Card(i, j)
                self.cards.append(card)

    def shuffle(self):
        """
            Mélange le deck
        """
        random.shuffle(self.cards)


class Card:
    def __init__(self, sign, color):
        """
        Constructeur d'une carte
        :param sign:
        :param color:
        """
        self.sign = sign
        self.color = color
        self.value = signs.index(sign)

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ne__(self, other):
        return self.value != other.value

    def __str__(self):
        return "[{x},{y}]".format(x=self.sign, y=self.color)


class PresidentGame:
    #TODO nommage aleatoire des joueurs + nombre de joueur
    def __init__(self, players):
        self.players = players
        self.distribute_cards()

    def distribute_cards(self):
        deck = Deck()
        deck.shuffle()
        next_player = 0
        for i in deck.cards:
            self.players[next_player].add_to_hand(i)
            if next_player == len(self.players)-1:
                next_player = 0
            else:
                next_player += 1


class Player:

    def __init__(self, name="default"):
        self.name = name
        self.hand = []

    def add_to_hand(self, card: Card):
        self.hand.append(card)

    def remove_from_hand(self, card: Card):
        self.hand.pop(card)

    #TODO fonction de tri de main

    def play(self, card: Card):
        pass


class Round:
    def __init__(self, nb_card_to_play, next_player):
        self.nb_card_ti_play = nb_card_to_play
        self.next_player = next_player
        self.trick: Card = []

