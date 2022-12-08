import names
from AIPlayer import AIPlayer
from president import PresidentGame
from player import Player

print("lancement Président")
nb_player = int(input('Entrez un nombre de joueurs: '))
players = []
name_player = input('Entrez le nom du joueur: ')
players.append(Player(name_player))
for i in range(nb_player-1):
    name_player = names.get_full_name()
    players.append(AIPlayer(name_player))
for i in players:
    i.display_hand()
game = PresidentGame(players)
game.start()




