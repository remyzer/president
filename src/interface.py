from models import *
import names

print("lancement Président")
nb_player = int(input('Entrez un nombre de joueurs: '))
players = []
name_player = input('Entrez le nom du joueur: ')
players.append(Player(name_player))
for i in range(nb_player-1):
    name_player = names.get_full_name()
    players.append(Player(name_player))
game = PresidentGame(players)




next_player = game.find_heart_queen_in_player_hand(players)
next_player.display_hand()



