import unittest
import names

from AIPlayer import AIPlayer
from deck import Deck
from player import Player
from president import PresidentGame


class TestCardsExercice2(unittest.TestCase):
    def test_player_constructor(self):
        player_trump = Player('Trump')
        self.assertTrue(player_trump.name == 'Trump')

    def test_incognito_player_should_have_random_name(self):
        player_incognito = Player()
        self.assertFalse(player_incognito.name == '')

    def test_default_game_has_three_players(self):
        players = []
        for _ in range(3):
            name_player = names.get_full_name()
            players.append(AIPlayer(name_player))
        game = PresidentGame(players)
        self.assertTrue(len(game.players) == 3)

    def test_game_launch_distributes_cards(self):
        """ Game generation should distribute cards evenly. """
        players = []
        for _ in range(3):
            name_player = names.get_full_name()
            players.append(AIPlayer(name_player))
        game = PresidentGame(players)
        player_1 = game.players[0]
        player_2 = game.players[1]
        self.assertTrue(len(player_1.hand) > 0)
        self.assertTrue(len(player_1.hand) >= len(player_2.hand))

    def test_afficher_deck(selfself):
        deck = Deck()
        for i in deck.cards:
            print(i)



if __name__ == '__main__':
    unittest.main()

