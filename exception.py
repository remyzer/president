"""
Module avec les Exceptions
"""


class InvalidNumberOfPlayerError(Exception):
    """
    Exception pour la saisie d'un nombre de joueur incorrect
    """


class InvalidNumberOfCardException(Exception):
    """
    Exception pour le mauvais nombre de carte à jouer
    """


class InvalidCardToPlayException(Exception):
    """
    Exception pour le saisie de carte hors de la main
    """
