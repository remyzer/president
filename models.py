import random


colors = ['♠', '♣', '♦', '♥']

signs = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']


class Deck:
    def __init__(self):
        self.cards = []
        for i in signs:
            for j in colors:
                card = Card(i, j)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)


class Card:
    def __init__(self, sign, color):
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


class Player:

    def __init__(self, name="default"):
        self.name = name
        self.hand = []

    def add_to_hand(self, card: Card):
        self.hand.append(card)

    def remove_from_hand(self, card: Card):
        self.hand.pop(card)

    def play(self, card: Card):
        pass