"""
Module lié à la création de Deck
"""
import dataclasses
import random

from card import Card

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
