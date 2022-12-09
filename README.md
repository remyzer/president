# President Game

Le président (aussi appelé le troufion) est un jeu de cartes rapide et amusant, au cours duquel la hiérarchie des joueurs changera à chaque manche. Le vainqueur d'une manche devient le président, alors que le perdant est proclamé troufion. Une fois que vous maitriserez les règles de base, vous pourrez essayer différentes variantes de ce jeu très populaire.

## Règles du jeu :

Ce jeu se joue de 3 à 6 joueurs.
Lors du premier tour, le joueur possédant la dame de coeur commence.
L'ensemble des cartes sont distribuées aux joueurs de la manière la plus homogène.
Ce jeu se joue par tours. Tant que quelqu'un peut et veut jouer, le tour continue et tourne dans le sens horaire.
Le premier joueur choisit des cartes d'une même valeur et les pose sur la table.
Suite à ça, chaque joueur doit jouer le même nombre de cartes d'une valeur égale ou supérieure.
Un joueur a le droit de sauter son tour et reprendre le tour d'après.
Un tour est fini lorsque plus personne ne peux jouer sur la dernière carte jouée, ou si un joueurs place un 2, ce qui met fin au tour. C'est alors le dernier à avoir joué qui ouvre la manche suivante.
L'objectif est d'être le premier à ne plus avoir de cartes. Ce joueur est alors déclaré président de la manche.
Les joueurs restants continuent à jouer jusqu'à ce qu'il n'y ait plus qu'une joueur qui ait des cartes en main, il est alors déclaré 'troufion'

On décide alors ou non de jouer une nouvelle manche. Ce sera le troufion qui ouvrira la partie.

## Organisation du code

Le code est réparti en 6 modules: \
-Un module Card qui permet la création d'une carte, et la comparaisons des cartes par la valeur \
-Un module Deck qui gère la création des 52 cartes du deck et le mélange du deck \
-Un module ai_player gère un joueur IA et le fait jouer automatiquement
L' IA joue 1 ou plusieurs cartes (jusqu'à 4) avec la valeur la plus faible,
dans un tour où on joue une seule carte, elle va jouer sa carte la plus faible même si cette carte casse une paire/triple/carré \
-Un module player où l'on va retrouver toutes les méthodes qui ont une influence sur la main (la trier, l'afficher, enlever une carte, ajouter une carte)
Le déroulement d'un tour se passe principalement dans la méthode play() avec des intéractions en console \
-Un module President qui initialise le jeu, distribue les cartes, définit le premier joueur qui doit jouer en trouvant celui qui détient la dame de coeur
La méthode start() lance la partie, qui sera un enchaînement de rounds\
-Un module round permet la gestion des rounds, le constructeur prend en arguments une liste de joueurs, la méthode start() va demander au premier joueur de jouer, puis il va trouver le joueur suivant en suivant l'ordre de la liste.
Round gère également les conditions d'arrêt d'un round, il faut que trois joueurs passent leur tour ou que l'un des joueurs joue une ou plusieurs cartes 2 \

Le main permet de gérer les paramètres de la partie : la création des joueurs, le nombre de joueurs, et le pseudo du joueur humain avant de lancer un president game.


## Explication de l' affichage

Pour lancer le jeu on doit lancer le main.py
Au lancement de la partie on nous demande le nombre de joueurs,\
Ensuite on demande le nom du joueur
Ensuite à chaque round on affiche le nom des joueurs avec l'évolution de leurs cartes
Quand arrive le tour du player humain on affiche les dernières cartes jouées et la main du joueur humain pour qu'il puisse choisir ce qu'il veut jouer
Si on commence le round (dame de coeur ou gagnant du round précédent), on peut choisir le nombre de carte pour commencer le round.\
Ensuite on peut choisir les cartes à jouer en sélectionnant leurs index dans la main.