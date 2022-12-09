# President Game

Le président (aussi appelé le troufion) est un jeu de cartes rapide et amusant, au cours duquel la hiérarchie des joueurs changera à chaque manche. Le vainqueur d'une manche devient le président, alors que le perdant est proclamé troufion. Une fois que vous maitriserez les règles de base, vous pourrez essayer différentes variantes de ce jeu très populaire.

## Règles du jeu :

Ce jeu se joue de 3 à 6 joueurs.
Lors du premier tour, le joueur possédant la dame de coeur commence.
L'ensemble des cartes sont distribuées aux joueurs de la manière la plus homogène.
Ce jeu se joue par tours. Tant que quelqu'un peut et veut jouer, le tour continue et tourne dans le sens horaire.
Le premier joueur choisit des cartes d'une même valeur et les pose sur la tables.
Suite à celà, chaque joueur doit fournir autant de cartes que le joueur précédent des cartes dun' valeur supérieure ou égale.
Un joueur a le droit de sauter son tour et reprendre le tour d'après.
Un tour est fini lorsque plus personne ne joue. C'est alors le dernier à avoir joué qui ouvre la manche suivante. Ou si un joueur pose un ou plusieurs deux. Ce qui mets immédiatement fin au tour.
L'objectif est d'être le premier à ne plus avoir de cartes. Ce joueur est alors déclaré président de la manche.
Les joueurs restants continuent à jouer jusqu'à ce qu'il n'y ait plus qu'une joueur qui ait des cartes en main, il est alors déclaré 'troufion'

On décide alors ou non de jouer une nouvelle manche. Ce sera le troufion qui ouvrira la partie.

## Organisation du code

Le code est répartie en 6 modules: \
-Un module Card qui gére l'objet card et toutes ses méthodes magiques \
-Un module Deck qui gère la création des 52 cartes du deck et le mélange du deck \
-Un module ai_player où on va trouver tout les méthodes de l' IA concernant quelles cartes elle va jouer 
L' IA actuelle joue la pair le triple ou le carré le plus faible possible qu'elle peut jouer
si elle à le choix elle va choisir de jouer une carte la plus faible. \
-Un module player où l'on va retrouver toutes les méthodes qui ont une influence sur la main (la trié, l'afficher, enlever une carte, ajouter une carte)
Actuellement on a crée une interaction console dans la méthode play de cette classe du au manque d'interface graphique. \
-Un module President qui initialise le jeu distribue les cartes trouve qui a la dame de coeur pour trouver qui doit commencer
et ensuite lancer la partie qui est un enchaînement de round (voir module suivant)\
-Un module round qui va lancer un round c'est à dire faire jouer le joueur qui a la dame de coeur puis trouver le joueur suivant (on joue dans l'ordre des position du tableau) le faire jouer etc.
Il va aussi gérer les conditions d'arrêt du round qui est que trois joueurs d'affilés ont passé ou alors si un joueur a joué un ou plusieurs 2 \

Le main permet de gérer les paramètres de la partie la création des joueurs, le nombre de joueurs, et le pseudo du joueur humain avant de lancer un president game.


## Explication de l' affichage

Au lancement de la partie on nous demande le nombre de joueurs,\
Ensuite on demande le nom du joueur
Ensuite à chaque round on affiche le nom des joueurs avec l'évolution de leurs cartes
Quand arrive le tour du player humain on affiche les dernières cartes jouées et la main du joueur humain pour qu'il puisse choisir ce qu'il veut jouer
Si on commence le round (dame de coeur ou gagnant du round précédent), on peut choisir le nombre de carte pour commencer le round.\
Ensuite on peut choisir les cartes à jouer en sélectionnant leurs index dans la main.