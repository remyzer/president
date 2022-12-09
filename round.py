"""
Module gérant un tour de jeu
"""


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
        Lancement du round
        :return: le joeur qui à gagner le round
        """
        number_of_players_to_pass = 0
        #Condition d'arrêt du round si trois joueur d'affilés ont passé
        while number_of_players_to_pass < len(self.players)-1:
            self.display_number_of_cards_per_players()
            #On fait jouer un joueur et on récupère ses cartes jouées
            cards_play = self.next_player.play(self.last_cards_played)
            #Si un joueur retourne une liste vide c'est qu'il a passé
            if len(cards_play) == 0:
                number_of_players_to_pass += 1
            else:
                number_of_players_to_pass = 0
                self.last_cards_played = cards_play
                #Condition d'arrêt si jamais un joueur joue un ou plusieurs 2
                if self.last_cards_played[0].value == 12:
                    break
            self.next_player = self.find_next_player()
        print(f"Gagnant du round: {self.next_player.name}")
        return self.next_player

    def find_next_player(self):
        """
        L'ordre de jeu est l'ordre des joueurs dans la liste quand
        on arrive à la fin on recommence au début
        :return: Retourne le prochain joueur qui doit jouer
        """
        if self.players.index(self.next_player) == len(self.players) - 1:
            return self.players[0]
        return self.players[self.players.index(self.next_player)+1]

    def display_number_of_cards_per_players(self):
        """
        Affiche le nombre de cartes de chaque joueur
        :return:
        """
        player_list_card = ""
        for player in self.players:
            player_list_card += f"{player.name}:{len(player.hand)} cartes "
        print(player_list_card)
