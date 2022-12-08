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