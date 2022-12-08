from deck import Deck
from round import Round


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
        while self.number_of_player_with_empty_hand() < len(self.players) - 1:
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
