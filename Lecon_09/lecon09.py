import random

def saisie_nombre():
    while True:
        nch = input("Donner un nombre de quatre chiffres : ")
        if nch.isdigit():
            n = int(nch)       
            if 1000 <= n <= 9999:
                return n
        print("Saisie incorrecte!")


def compter_chiffres(n):
    nch = str(n)
    nci = 0
    for c in nch:
        if c in ['1', '3', '5', '7', '9']:
            nci += 1
    return nci


# Programme principal
sj1, sj2 = 0, 0
for i in range(3):
    print('Tour', (i+1))
    
    j1 = saisie_nombre()
    j2 = random.randint(1000, 9999)

    p = j1 * j2

    print("Choix joueur : %d - Choix ordinateur : %d" % (j1, j2))
    print("%d * %d = %d" % (j1, j2, p))

    nci = compter_chiffres(p)
    print("Le nombre de chiffres impairs :", nci)

    if nci % 2 == 1:
        print('Le nombre de chiffres impairs est impair. Vous gagnez!')
        sj1 += 1
    else:
        print('Le nombre de chiffres impairs est pair. Vous perdez!')
        sj2 += 1

if sj1 > sj2:
    print('Vous avez gagné au jeu : %d contre %d' % (sj1, sj2))
else:
    print('Vous avez perdu au jeu :  %d contre %d' % (sj1, sj2))