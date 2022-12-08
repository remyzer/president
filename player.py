from card import Card


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
        self.display_last_cards_play(last_cards_play)
        self.display_hand()
        if len(last_cards_play) == 0:
            number_of_cards_to_play = int(input("Combien de Cartes voulez vous jouer?"))
        else:
            number_of_cards_to_play = len(last_cards_play)
        for _ in range(number_of_cards_to_play):
            card_to_play = \
                int(input("Quelle carte voulez vous jouer?(index du tableau -1 pour passer)"))
            if card_to_play == -1:
                return []
            cards_to_played.append(self.hand[card_to_play])
        # On vérifie que tous les élément de la liste sont de même valeur
        if cards_to_played.count(cards_to_played[0]) == len(cards_to_played):
            # On vérifie que les cartes sélectionner à jouer sont valable
            # en fonction de ce qui a été joué avant
            if len(last_cards_play) == 0 or cards_to_played[0] >= last_cards_play[0]:
                for card in cards_to_played:
                    self.remove_from_hand(card)
                return cards_to_played
        return []

    @staticmethod
    def display_last_cards_play(last_cards_play):
        """
        Affiche la liste des dernières cartes jouées
        :param last_cards_play: liste des cartes jouées
        """
        last_trick = ""
        for card in last_cards_play:
            last_trick += f"[{card.sign},{card.color}]"
        print("Dernière cartes jouées : " + last_trick)
