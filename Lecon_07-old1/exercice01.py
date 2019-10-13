import random

CHOIX = ['Ciseaux', 'Feuille', 'Pierre']


def bat(j1, j2):
    return ((j2 - j1) % 3) == 1


def choix_joueur():
    while True:
        try:
            j1 = int(input(('\n'.join('{}. {}'.format(i, CHOIX[i]) for i in range(
                len(CHOIX))) + '\nQuel est votre choix ? ')))
            if 0 <= j1 <= 2:
                return j1
        except:
            pass
        print('> Choix incorrect')


def gagnant(pia, pj1):
    if pia > pj1:
        print('Vous avez perdu {} contre {}'.format(pia, pj1))
    elif pia < pj1:
        print('Vous avez gagné {} contre {}'.format(pj1, pia))
    else:
        print('Match nul')

##########################################################
# Programme Principal


print('Jeu Pierre - Ciseaux - Feuille')

pia, pj1 = 0, 0
for i in range(3):
    print()
    j1 = choix_joueur()
    ia = (j1 + 1) % 3

    if bat(j1, ia):
        print('\nJoueur gagne : {} bat {}'.format(CHOIX[j1], CHOIX[ia]))
        pj1 += 1
    elif bat(ia, j1):
        print('\nOrdinateur gagne : {} est battu(e) par {}'.format(
            CHOIX[j1], CHOIX[ia]))
        pia += 1
    else:
        print('\nManche nulle : {} et {} match nul.'.format(
            CHOIX[j1], CHOIX[ia]))

print('\nLe jeu est terminé')
gagnant(pia, pj1)
