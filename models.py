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
    """
    Distribue équitablement les cartes entre tous les joueurs
    """
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
    """
    Trouve le joueur avec la dame de coeur dans sa main
    :parameter List of Players: players
    """
    def find_heart_queen_in_player_hand(self, players):
        for player in players:
            for card in player.hand:
                if card.sign == 'Q' and card.color == '♥':
                    return player


class Player:

    def __init__(self, name="default"):
        """
        Constructeur de la classe Player
        :param name:
        """
        self.name = name
        self.hand = []
        self.role = ''

    def add_to_hand(self, card: Card):
        """
        Ajoute une carte à la main du joueur
        :param card: carte à ajouter
        """
        self.hand.append(card)

    def remove_from_hand(self, card: Card):

        """
         Retire la carte de la main du joueur
        :param card:  carte à retirer
        """
        index = self.hand.index(card)
        self.hand.pop(index)

    def sort_hand_by_value(self):
        """
        Trie les cartes du joueur de la plus faible à la plus forte
        """
        self.hand = sorted(self.hand)
    @staticmethod
    def check_if_multiple_cards_are_equals(cards):
        """
        Vérifie si les cartes jouées en même temps sont bien les mêmes
        :param cards: List of Cards
        """
        previous_card = cards[0].value
        for card in cards:
            if card.value != previous_card.value:
                raise CardsNotEqual("Les cartes jouées ne sont pas égales")
    def display_hand(self):
        """
        Affiche dans la console la main du joueur
        :return:
        """
        hand_string = ""
        for card in self.hand:
            hand_string += f"{card.sign}{card.color}|"
        print(hand_string)

    def play(self, hand_index):
        """
        Retire de la main du joueur les cartes jouées
        :param hand_index:
        :return: retourne les cartes jouées
        """
        cards_played = []
        for index in hand_index:
            cards_played.append(self.hand[index])
            self.remove_from_hand(self.hand[index])
        self.check_if_multiple_cards_are_equals(cards_played)
        return cards_played


class Round:
    def __init__(self, next_player, players):
        self.players = players
        self.nb_card_to_play = 0 #FIXME a modifier
        self.next_player = next_player
        self.trick = []
        self.last_cards_played = []
        while True :
            if self.next_player.type() == AIPlayer:
                self.next_player.play(self.last_cards_played)
            else:
                self.next_player.play()



class AIPlayer(Player):

    def play(self, last_cards_play):
        """
        Joue la ou les premiere(s) carte(s) que l'AI peut jouer
        :param last_cards_play: dernières cartes jouées
        :return:
        """
        cards_played = []
        i = 0
        if last_cards_play is not None:
            while last_cards_play[0].value > self.hand[i].value:
                i+=1
        cards_played.append(self.hand[i])
        self.hand.pop(i)
        while self.hand[i].value == cards_played[i].value:
            cards_played.append(self.hand[i])
            self.hand.pop(i)
        return cards_played

    #TODO fonction pour redoonner la premiere combinaison jouable
    def first_combination_playable(self, last_cards_play):
        """
        Choisi la plus faible combinaison de cartes jouable
        :param last_cards_play: dernières cartes jouées
        :return: liste de cartes
        """
        cards_to_play = last_cards_play.length()
        if 0 == self.hand.length():
            return []
        elif cards_to_play == 0 :
            result = [self.hand[0]]
            self.remove_from_hand(self.hand[0])
            return result
        else:
            result = []
            index = 0
            while True:

            for card in self.hand:
                if card > last_cards_play[0] and :



