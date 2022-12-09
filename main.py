"""
Module parametrant le lancement de la partie
"""
import names

from ai_player import AIPlayer
from president import PresidentGame
from player import Player

if __name__ == '__main__':
    print("****************")
    print("JEU DU PRESIDENT")
    print("****************")
    nb_player = 0
    error = "start"
    while error != "":
        try:
            nb_player = int(input('Entrez un nombre de joueurs: (entre 3 et 6)'))
            if nb_player < 3 or nb_player > 6:
                raise Exception
        except Exception:
            error = "nombre de player invalide"
            print(error)
        else:
            error = ""
    players = []
    name_player = input('Entrez votre pseudo: ')
    #Ajout du joueur humain
    players.append(Player(name_player))
    #Création et ajout des IA
    for i in range(nb_player - 1):
        name_player = names.get_full_name()
        players.append(AIPlayer(name_player))
    #Création et démarrage de la partie
    game = PresidentGame(players)
    game.start()
