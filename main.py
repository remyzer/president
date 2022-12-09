"""
Module parametrant le lancement de la partie
"""
import names
from ai_player import AIPlayer
from president import PresidentGame
from player import Player
print("****************")
print("JEU DU PRESIDENT")
print("****************")
nb_player = int(input('Entrez un nombre de joueurs: '))
players = []
name_player = input('Entrez votre pseudo: ')
players.append(Player(name_player))
for i in range(nb_player-1):
    name_player = names.get_full_name()
    players.append(AIPlayer(name_player))
game = PresidentGame(players)
game.start()





