from player import Player


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
                # on remove les cartes en ordre décroissant pour éviter les probleme d'index.
                self.remove_from_hand(self.hand[index + 1])
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
                # on remove les cartes en ordre décroissant pour éviter les probleme d'index.
                self.remove_from_hand(self.hand[index + 2])
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
            if self.hand[index] == self.hand[index + 1] == self.hand[index + 2] == \
                    self.hand[index + 3] and self.hand[index] > last_cards_play[0]:
                card_to_play.append(self.hand[index])
                card_to_play.append(self.hand[index + 1])
                card_to_play.append(self.hand[index + 2])
                card_to_play.append(self.hand[index + 3])
                # on remove les cartes en ordre décroissant pour éviter les probleme d'index.
                self.remove_from_hand(self.hand[index + 3])
                self.remove_from_hand(self.hand[index + 2])
                self.remove_from_hand(self.hand[index + 1])
                self.remove_from_hand(self.hand[index])
                return card_to_play
            index += 1
        return card_to_play
