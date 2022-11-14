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
    def __init__(self):
        messi = Player('Messi')
        neymar = Player('Neymar')
        mbappe = Player('Mbappe')
        self.players = [messi, neymar, mbappe]
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

    def find_heart_queen_in_player_hand(self, players):
        for player in players:
            for card in player.hand:
                if card.sign == 'Q' and card.color == '♥':
                    return player

class Player:

    def __init__(self, name="default"):
        self.name = name
        self.hand = []
        self.role = ''

    def add_to_hand(self, card: Card):
        self.hand.append(card)

    def remove_from_hand(self, card: Card):
        self.hand.pop(card)

    def sort_hand_by_value(self):
        self.hand = sorted(self.hand)

    def check_if_multiple_cards_are_equals(self, cards):
        pass

    def display_hand(self):
        hand_string = ""
        for card in self.hand:
            hand_string += f"{card.sign} {card.color}|"
        print(hand_string)

    def play(self, hand_index):
        cards_played = []
        # TODO Methode pour tester si les paires et plus ont des valeurs identiques
        for index in hand_index:
            cards_played.append(self.hand[index])
            self.remove_from_hand(self.hand[index])
        return cards_played
