import unittest

from ai_player import AIPlayer
from card import Card


class TestAIPlayer(unittest.TestCase):
    def test_AIPlayer_play(self):
        player = AIPlayer()
        c1 = Card('3', '♥')
        c2 = Card('3', '♦')
        c3 = Card('3', '♣')
        c4 = Card('4', '♥')
        c5 = Card('5', '♥')
        c6 = Card('5', '♠')
        c7 = Card('7', '♥')
        last_cards_play = [c1, c2]
        player.hand = [c3, c4, c5, c6, c7]
        resultat_attendu = [c5, c6]
        self.assertEqual(player.play(last_cards_play), resultat_attendu)

    def test_AIPlayer_play_2(self):
        player = AIPlayer()
        c1 = Card('3', '♥')
        c2 = Card('3', '♦')
        c3 = Card('3', '♣')
        c4 = Card('4', '♥')
        c5 = Card('5', '♥')
        c6 = Card('5', '♠')
        c7 = Card('7', '♥')
        c8 = Card('5', '♣')
        last_cards_play = [c1, c2, c3]
        player.hand = [c4, c5, c6, c8, c7]
        resultat_attendu = [c5, c6, c8]
        self.assertEqual(player.play(last_cards_play), resultat_attendu)

    def test_AIPlayer_play_3(self):
        player = AIPlayer()
        c1 = Card('3', '♥')
        c2 = Card('3', '♦')
        c3 = Card('3', '♣')
        c4 = Card('4', '♥')
        c5 = Card('5', '♥')
        c6 = Card('5', '♠')
        c7 = Card('7', '♥')
        c8 = Card('5', '♣')
        last_cards_play = [c1]
        player.hand = [c4, c5, c6, c8, c7]
        resultat_attendu = [c4]
        self.assertEqual(player.play(last_cards_play), resultat_attendu)
