from tkinter import *
from tkinter import messagebox
import os
import random


def charger_image(nom):
    """Permet de charger un fichier GIF"""
    dir = os.path.dirname(__file__)
    return PhotoImage(file=os.path.join(dir, nom))


def image_lbl(label, image):
    """Change l'image d'arrrière plan d'un label"""
    label.configure(image=image)


def afficher_scores(sj, so):
    """Affiche les scores des joueurs"""
    lbl_sj1.configure(text="{}".format(sj))
    lbl_sj2.configure(text="{}".format(so))


def afficher_essais(essais):
    """Afficher le nombre d'essais restants"""
    lbl_essais.configure(text='Essais\n{}'.format(essais))


fenetre = Tk()
fenetre.title('Ciseaux - Feuille - Pierre')

CISEAUX, FEUILLE, PIERRE = 0, 1, 2
MAX_ESSAIS = 3

TEXTES = [
    'Ciseaux',
    'Feuille',
    'Pierre'
]

IMAGES = [
    charger_image('ciseaux.gif'),
    charger_image('feuille.gif'),
    charger_image('pierre.gif')
]

RIEN, VERSUS = charger_image('rien.gif'), charger_image('versus.gif')

sj, so = 0, 0
essais = MAX_ESSAIS


def bat(j1, j2):
    """Retourne True uniquement si le choix de j1 est gagnant"""
    return (j1 == CISEAUX and j2 == FEUILLE) or\
        (j1 == FEUILLE and j2 == PIERRE) or\
        (j1 == PIERRE and j2 == CISEAUX)


def gagnant(cj1, cj2):
    """Retourne 1 si le premier joueur gagne un coup
    Retourne -1 si le deuxième joueur gagne un coup
    Retourne 0 en cas d'égalité"""
    if bat(cj1, cj2):
        return 1
    elif bat(cj2, cj1):
        return -1
    else:
        return 0


def afficher_gagnant(sj1, sj2):
    """Affiche le gagnant selon le score"""
    if sj1 > sj2:
        message = "Vous êtes gagnant!"
    elif sj1 < sj2:
        message = "Vous êtes perdant!"
    else:
        message = "Partie nulle!"
    lbl_gagnant.configure(text=message)


def afficher_gagnant_manche(cj, co):
    global sj, so
    num_gagnant = gagnant(cj, co)
    if num_gagnant == 1:
        message = '{} bat {}'.format(TEXTES[cj], TEXTES[co])
        fg = '#006600'
        sj += 1
    elif num_gagnant == -1:
        message = '{} est battu par {}'.format(TEXTES[cj], TEXTES[co])
        fg = '#ff0000'
        so += 1
    else:
        message = '{} et {} manche nulle'.format(TEXTES[cj], TEXTES[co])
        fg = '#0000ff'
    lbl_resultat.configure(text=message, fg=fg)


def jouer(cj):
    global sj, so, essais

    co = random.randint(0, 2)

    image_lbl(lbl_cj1, IMAGES[cj])
    image_lbl(lbl_cj2, IMAGES[co])

    afficher_gagnant_manche(cj, co)
    afficher_gagnant(sj, so)
    afficher_scores(sj, so)

    essais -= 1
    afficher_essais(essais)

    if essais == 0:
        if messagebox.askyesno('Partie terminée', 'Voulez-vous recommencer ?'):
            rejouer()
        else:
            fenetre.destroy()
        return


def rejouer():
    global sj, so, essais

    sj, so = 0, 0
    afficher_scores(sj, so)

    essais = MAX_ESSAIS
    afficher_essais(essais)
    lbl_gagnant.configure(text="")
    lbl_resultat.configure(text="")

# -----------------------------------------------------------------------------
# Interface de l'application
# -----------------------------------------------------------------------------


# Score utilisateur
lbl_j1 = Label(fenetre, text='Utilisateur', font=('Garamond', 16))
lbl_j1.grid(row=0, column=0)

lbl_sj1 = Label(fenetre, text='0', font=('Garamond', 16))
lbl_sj1.grid(row=1, column=0)

# Score ordinateur
lbl_j2 = Label(fenetre, text='Ordinateur', font=('Garamond', 16))
lbl_j2.grid(row=0, column=2)

lbl_sj2 = Label(fenetre, text='0', font=('Garamond', 16))
lbl_sj2.grid(row=1, column=2)

# Choix de l'utilisateur
lbl_cj1 = Label(fenetre, image=RIEN)
lbl_cj1.grid(row=2, column=0)

lbl_vs = Label(fenetre, image=VERSUS)
lbl_vs.grid(row=2, column=1)

# Choix de l'ordinateur
lbl_cj2 = Label(fenetre, image=RIEN)
lbl_cj2.grid(row=2, column=2)

lbl_essais = Label(fenetre,
                   text='Essais\n{}'.format(essais), font=('Garamond', 20))
lbl_essais.grid(row=0, column=1, rowspan=2)

lbl_resultat = Label(fenetre, text="", fg="#ff0000",
                     font=('Garamond', 18))
lbl_resultat.grid(row=3, column=0, columnspan=3, pady=10)

lbl_gagnant = Label(fenetre, text="", fg="#ff6600",
                    font=('Garamond', 18))
lbl_gagnant.grid(row=4, column=0, columnspan=3, pady=5)

lbl_consigne = Label(
    fenetre, text='Pour jouer, cliquer sur une des icônes suivantes.')
lbl_consigne.grid(row=5, column=0, columnspan=3, pady=10)

# bouton ciseaux
btn_ciseaux = Button(
    fenetre, image=IMAGES[CISEAUX], command=lambda: jouer(CISEAUX))
btn_ciseaux.grid(row=7, column=0)

lbl_ciseaux = Label(fenetre, text=TEXTES[CISEAUX])
lbl_ciseaux.grid(row=6, column=0)

# bouton feuille
btn_feuille = Button(
    fenetre, image=IMAGES[FEUILLE], command=lambda: jouer(FEUILLE))
btn_feuille.grid(row=7, column=1)

lbl_feuille = Label(fenetre, text=TEXTES[FEUILLE])
lbl_feuille.grid(row=6, column=1)

# bouton pierre
btn_pierre = Button(
    fenetre, image=IMAGES[PIERRE], command=lambda: jouer(PIERRE))
btn_pierre.grid(row=7, column=2)

lbl_pierre = Label(fenetre, text=TEXTES[PIERRE])
lbl_pierre.grid(row=6, column=2)

mainloop()
