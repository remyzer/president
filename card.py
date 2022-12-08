signs = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']


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
