"""
Ce module contient toutes les classes relatives au jeu du président
"""
import dataclasses
import random

colors = ['♠', '♣', '♦', '♥']

signs = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']


@dataclasses.dataclass
class Deck:
    """
    Cette classe gère la distribution et le mélange du deck.
    """
    def __init__(self):
        """
        Initialise le Deck en créant les 52 cartes.
        """
        self.cards = []
        for i in signs:
            for j in colors:
                card = Card(i, j)
                self.cards.append(card)

    def shuffle(self):
        """
        Mélange le deck.
        """
        random.shuffle(self.cards)


class Card:
    """
    Cette classe permet la création et la comparaison de cartes uniquement par la valeur.
    """
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
        return f"[{self.sign},{self.color}]"


class PresidentGame:
    """
    Cette classe s'occupe de gérer la partie
    """
    def __init__(self, players):
        self.players = players
        self.distribute_cards()
        self.next_player = self.find_heart_queen_in_player_hand(self.players)
        for player in self.players:
            player.sort_hand_by_value()

    def start(self):
        """
        Cette méthode marque le début d'une partie.
        Elle s'arrête lorsqu'il ne reste plus qu'un joueur avec des cartes
        """
        while self.number_of_player_with_empty_hand() < len(self.players)-1:
            next_round = Round(self.next_player, self.players)
            self.next_player = next_round.start()

    def number_of_player_with_empty_hand(self):
        """
        Recherche le nombre de joueurs qui ont gagné
        :return: Le nombre de joueurs qui ont gagné
        """
        number_of_player_with_empty_hand = 0
        for player in self.players:
            if len(player.hand) == 0:
                number_of_player_with_empty_hand += 1
        return number_of_player_with_empty_hand

    def distribute_cards(self):
        """
        Distribue équitablement les cartes entre tous les joueurs
        """
        deck = Deck()
        deck.shuffle()
        next_player = 0
        for i in deck.cards:
            self.players[next_player].add_to_hand(i)
            if next_player == len(self.players) - 1:
                next_player = 0
            else:
                next_player += 1

    @staticmethod
    def find_heart_queen_in_player_hand(players):
        """
        Trouve le joueur avec la dame de coeur dans sa main
        :parameter players: List of Players
        :return: Le joueur possédant la dame de coeur
        """
        player_with_heart_queen = None
        for player in players:
            for card in player.hand:
                if card.sign == 'Q' and card.color == '♥':
                    player_with_heart_queen = player
        return player_with_heart_queen


class Player:
    """
    Cette classe permet la gestion de la main ,et des tours de jeu des différents joueurs
    """
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

    def display_hand(self):
        """
        Affiche dans la console la main du joueur
        :return:
        """
        hand_string = ""
        for card in self.hand:
            hand_string += f"{card.sign}{card.color}|"
        print(hand_string)

    def play(self, last_cards_play):
        """
        Demande au player quelle carte jouer
        :param last_cards_play: listes des dernieres cartes jouées vide si début du pli
        :return: retourne les cartes jouées
        """
        cards_to_played = []
        last_trick = ""
        for card in last_cards_play:
            last_trick += f"[{card.sign},{card.color}]"
        print("Dernière cartes jouées : " + last_trick)
        self.display_hand()
        if len(last_cards_play) == 0:
            number_of_cards_to_play = int(input("Combien de Cartes voulez vous jouer?"))
        else:
            number_of_cards_to_play = len(last_cards_play)
        for _ in range(number_of_cards_to_play):
            card_to_play = int(input("Quelle carte voulez vous jouer?(index du tableau -1 pour passer)"))
            if card_to_play == -1:
                return []
            cards_to_played.append(self.hand[card_to_play])
        if cards_to_played.count(cards_to_played[0]) == len(cards_to_played): #On vérifie que tous les élément de la liste sont de même valeur
            if len(last_cards_play) == 0 or cards_to_played[0] >= last_cards_play[0]: #On vérifie que les cartes sélectionner à jouer sont valable en fonction de ce qui a été joué avant
                for card in cards_to_played:
                    self.remove_from_hand(card)
                return cards_to_played
        return []


class Round:
    """
    Cette classe est utilisée pour la gestion des plis
    """
    def __init__(self, next_player, players):
        self.players = players
        self.next_player = next_player
        self.last_cards_played = []

    def start(self):
        """
        :return:
        """
        number_of_players_to_pass = 0
        while number_of_players_to_pass <= len(self.players):
            cards_play = self.next_player.play(self.last_cards_played)
            if len(cards_play) == 0:
                number_of_players_to_pass += 1
            else:
                number_of_players_to_pass = 0
                self.last_cards_played = cards_play
            if self.last_cards_played[0].value == 12:
                break
            self.next_player = self.find_next_player()
        return self.next_player

    def find_next_player(self):
        """
        :return: Retourne le prochain joueur qui doit jouer
        """
        if self.players.index(self.next_player) == len(self.players) - 1:
            return self.players[0]
        return self.players[self.players.index(self.next_player)+1]


class AIPlayer(Player):
    """
    Cette classe sert à la gestion des joueurs IA, c'est une classe fille de 'Player'
    """
    def play(self, last_cards_play):
        """
        Joue la ou les premiere(s) carte(s) que l'AI peut jouer
        :param last_cards_play: dernières cartes jouées
        :return: liste de carte à jouer liste vide s'il passe ou ne peut pas jouer
        """
        number_of_card_to_play = len(last_cards_play)
        match number_of_card_to_play:
            case 0:
                card_to_play = []
                if len(self.hand) != 0:
                    card_to_play = [self.hand[0]]
                return card_to_play
            case 1:
                return self.first_card_playable(last_cards_play)
            case 2:
                return self.first_pair_playable(last_cards_play)
            case 3:
                return self.first_triple_playable(last_cards_play)
            case 4:
                return self.first_four_playable(last_cards_play)
            case _:
                return []

    def first_card_playable(self, last_cards_play):
        """
        choisi la plus faible carte à jouer
        :param last_cards_play: liste de une carte
        :return: liste de deux cartes ou liste vide si jamais il n'y a pas de pair jouable
        """
        cards = []
        if len(self.hand) == 0:
            return []
        for card in self.hand:
            if card >= last_cards_play[0]:
                cards = [card]
            self.remove_from_hand(card)
            return cards
        return []

    def first_pair_playable(self, last_cards_play):
        """
        choisi la plus faible pair à jouer
        :param last_cards_play: liste de deux cartes
        :return: liste de deux cartes ou liste vide si jamais il n'y a pas de pair jouable
        """
        if len(self.hand) == 0:
            return []
        index = 0
        card_to_play = []
        while index + 1 < len(self.hand):
            if self.hand[index] == self.hand[index + 1] and self.hand[index] >= last_cards_play[0]:
                card_to_play.append(self.hand[index])
                card_to_play.append(self.hand[index + 1])
                self.remove_from_hand(self.hand[index + 1]) #on remove les cartes en ordre décroissant pour éviter les probleme d'index.
                self.remove_from_hand(self.hand[index])
                return card_to_play
            index += 1
        return card_to_play

    def first_triple_playable(self, last_cards_play):
        """
        choisi le triple le plus faible à jouer
        :param last_cards_play: liste de trois cartes
        :return: liste de trois cartes ou liste vide si jamais il n'y a pas de triple jouable
        """
        if len(self.hand) == 0:
            return []
        index = 0
        card_to_play = []
        while index + 2 < len(self.hand):
            if self.hand[index] == self.hand[index + 1] == self.hand[index + 2] \
                    and self.hand[index] > last_cards_play[0]:
                card_to_play.append(self.hand[index])
                card_to_play.append(self.hand[index + 1])
                card_to_play.append(self.hand[index + 2])
                self.remove_from_hand(self.hand[index + 2]) #on remove les cartes en ordre décroissant pour éviter les probleme d'index.
                self.remove_from_hand(self.hand[index + 1])
                self.remove_from_hand(self.hand[index])
                return card_to_play
            index += 1
        return card_to_play

    def first_four_playable(self, last_cards_play):
        """
        choisi le carré le plus faible à jouer
        :param last_cards_play: liste de quatres cartes
        :return: liste de quatre cartes ou liste vide si jamais il n'y a pas de carré jouable
        """
        if len(self.hand) == 0:
            return []
        index = 0
        card_to_play = []
        while index + 3 < len(self.hand):
            if self.hand[index] == self.hand[index + 1] == self.hand[index + 2] == self.hand[index + 3] \
                    and self.hand[index] > last_cards_play[0]:
                card_to_play.append(self.hand[index])
                card_to_play.append(self.hand[index + 1])
                card_to_play.append(self.hand[index + 2])
                card_to_play.append(self.hand[index + 3])
                self.remove_from_hand(self.hand[index + 3])  # on remove les cartes en ordre décroissant pour éviter les probleme d'index.
                self.remove_from_hand(self.hand[index + 2])
                self.remove_from_hand(self.hand[index + 1])
                self.remove_from_hand(self.hand[index])
                return card_to_play
            index += 1
        return card_to_play


class CardsNotEqual(Exception):
    """
    Classe fille de 'Exception', utilisée lors que plusieurs cartes jouées ne sont pas égales
    """
