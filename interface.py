from models import *

print("lancement Président")
nb_player = int(input('Entrez un nombre de joueurs: '))
players = []
for i in range(nb_player):
    name_player = input('Entrez le nom du joueur: ')
    players.append(Player(name_player))
game = PresidentGame(players)


