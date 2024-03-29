# Pensée computationnelle et programmation

## Séance du Jeudi 19/09/2019 : Leçon 1

Au début de la séance, j'ai présenté le curricula, la méthode de travail et les principaux outils qu'on utilisera au cours de l'année.

Après la prise de contact, j'ai distribué aux élèves une liste de mots Informatiques supposées connus et les élèves ont essayé de les grouper par thème.

## Séance du Samedi 21/09/2019 : Leçon 2

Dans la deuxième leçon nous avons commencé par décomposer l'interface de l'application Tetris.

Nous avons ensuite étudié [un petit programme Tkinter](./Lecon_02/question_7.py)

![Résultat du programme](./images/lecon_02_q7.png)

Nous avons modifié le programme précédent pour dessiner les pièces de Tetris. [Le programme](./Lecon_02/question_8.py)

![Résultat du programme](./images/lecon_02_q8.png)

## Séance du Jeudi 26/09/2019 : Leçon 3

Dans la troisième séance, nous avons fait un rappel sur la séance précédente. Puis, nous avons présenté la pensée computationnelle tout en référant au Jeu Tetris.

Nous avons, par la suite, appliqué la pensée computationnelle afin de dessiner la figure d'une maison.

![Résultat leçon 3](./images/lecon_03.PNG)

[Solution](./Lecon_3/question_3.py)

## Séance du Samedi 28/09/2019 : Leçon 4

Dans la quatrième séance nous nous sommes intéressés à la grille du jeu. Nous avons déterminé les caractéristiques et les opérations de cette grille de jeu. 

Nous avons ensuite commencé par la première opération : Initialiser la grille du jeu.

Les élèves ont écrit un [programme](./Lecon_04/programme_v01.py) qui affiche la fenêtre suivante :

![Résultat leçon 4](./images/lecon_04.PNG)

## Séance du Mardi 01/10/2019 : Leçon 5

Dans la cinquième séance, nous avons commencé par présenter les structures conditionnelles **si ... alors ... sinon ... fin si** en Python à travers le programme qui détermine [Le plus agé](./Lecon_05/plus_age.py).

Ensuite, nous avons essayé de dessiner un feu de circulation. Nous avons utilisé des constantes dans le calcul des différentes dimensions utilisés afin de permettre une certaine flexibilité dans le [programme](./Lecon_05/programme_v02.py).


Pour ajouter de la vie à notre travail, nous avons utilisé un timer pour [faire clignoter les trois feux en même temps](./Lecon_05/programme_v03.py).

Notre programme a été, par la suite, amélioré :

* [La première amélioration](./Lecon_05/programme_v04.py) :         
  a. Le feu rouge s’allume pendant 5 secondes, puis s’éteint

  b. Le feu jaune s’allume pendant 1 seconde, puis s’éteint

  c. Le feu vert s’allume pendant 5 secondes, puis s’éteint

* [La deuxième amélioration](./Lecon_05/programme_v05.py) : Dans une situation réelle avant que le feu ne redevienne rouge une autre fois le feu jaune doit clignoter trois fois. Modifier votre programme afin de réaliser ce comportement.


| Première version | Deuxième version | Troisième version | Quatrième version |
| ---------------- | ---------------- | ----------------- | ----------------- |
| ![Résultat Programme](./images/lecon_05_01.PNG) | ![Résultat Programme](./images/lecon_05_02.gif) | ![Résultat Programme](./images/lecon_05_03.gif) | ![Résultat Programme](./images/lecon_05_04.gif) |
| [Code Source](./Lecon_05/programme_v02.py) | [Code Source](./Lecon_05/programme_v03.py) | [Code Source](./Lecon_05/programme_v04.py) | [Code Source](./Lecon_05/programme_v05.py) |


## Séance du Jeudi 03/10/2019 : Leçon 6

Dans le but d'implémenter une version simplifiée du fameux jeu Pierre - Ciseaux - Feuille, nous avons commencé par déterminer l'ensemble des objets (constantes & variables) du programme.

Etant décomposé en modules, nous avons introduit la notion de fonction et nous avons remarqué qu'elle peut avoir des paramètres.

Lors de la définition de l'ensemble des fonctions, nous avons utilisé la structure **répéter** ... **jusqu'à ...** pour le contrôle de saisie de l'utilisateur. Nous avons eu besoin de répéter une action un nombre défini de fois d'où l'utilisation de la structure **pour ... faire** ... **fin pour**.

Finalement, les élèves ont essayé de faire la traduction des algorithmes en Python et de réaliser un [programme fonctionnel](./Lecon_06/pcf.py).

Voici un exemple du fonctionnement du programme :

```
Jeu Pierre - Ciseaux - Feuille

0. Ciseaux
1. Feuille
2. Pierre
Quel est votre choix ? 1

Joueur gagne : Feuille bat Pierre

0. Ciseaux
1. Feuille
2. Pierre
Quel est votre choix ? 2

Ordinateur gagne : Pierre est battu(e) par Feuille

0. Ciseaux
1. Feuille
2. Pierre
Quel est votre choix ? 1

Manche nulle : Feuille et Feuille match nul.

Le jeu est terminé
Match nul
```

## Séance du Jeudi 10/10/2019 : Leçon 7

Nous avons profité de la connexion Internet, pour créer des comptes Google Classroom. Puis, nous avons fait une démonstration comment créer un programme Python sur repl.it, puis le remettre dans Google Classroom. 

Nous avons traité trois programme :

1. Le premier saisi deux entiers et affiche leurs sommes : [Lien](./Lecon_07/exercice01.py)

2. Le seconde convertit une température Celcius en Fahrenheit et inversement : [Lien](./Lecon_07/exercice02.py)

3. Le troisième affiche la table de multiplication : [Lien](./Lecon_07/exercice03.py)

## Séance du Jeudi 17/10/2019 : Leçon 8

Un élève souhaite calculer le temps qu'il a passé dans la révision de deux matières. On propose un algorithme et on demande de le traduire en Python. Par la suite le programme est testé avec des données correctes.

Puis, avec des données erronés, on remarque que le programme ne fonctionne pas correctement. On suggère, alors, le contrôle de saisie de l'utilisateur à travers une nouvelle fonction **saisie_heure(msg, hdm)** qui remplacera la simple saisie à l'aide d'**input**.

La version finale atteinte par les élèves à la fin de cette séance : [Lien](./Lecon_07/v01_eleve.py)

## Séance du Samedi 19/10/2019 : Leçon 8 (suite)

Le programme est amélioré d'avantage par une fonction **saisie_revision(matiere, hdm)** qui assure la saisie correcte de l'heure de début et de fin de révsision pour une matière donnée. Cette nouvelle se basera sur la fonction précédente **saisie_heure(msg, hdm)** et ajoutera un test pour que l'heure de fin de révision soit toujours supèrieure à l'heure de début de révision.

Comme l'élève cité précédemment puisse vouloir réviser pour plusieurs matières on demande d'améliorer le programme pour supporter un nombre donné de matières : [Lien](./Lecon_08/v04.py).

```
Donner le nombre de matières à réviser : 4
Matière n° 1
Donner le nom de la matière : info
Heure début de révision (info) >= 00:00 : 10:00
Heure de fin de révision (info) > 10:00 : 11:15
Matière n° 2
Donner le nom de la matière : tech
Heure début de révision (tech) >= 11:15 : 11:30
Heure de fin de révision (tech) > 11:30 : 12:10
Matière n° 3
Donner le nom de la matière : physique
Heure début de révision (physique) >= 12:10 : 13:00
Heure de fin de révision (physique) > 13:00 : 15:00
Matière n° 4
Donner le nom de la matière : math
Heure début de révision (math) >= 15:00 : 17:00
Heure de fin de révision (math) > 17:00 : 17:15
Temps de révision
info : 01:15
tech : 00:40
physique : 02:00
math : 00:15
Durée Totale : 04:10
```

