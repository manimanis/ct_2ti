from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random
from functools import partial

WIMAGE, HIMAGE = 217, 150
IMAGES_COUNT = 8
NROWS, NCOLS = 4, 4
MAX_ESSAIS = int(IMAGES_COUNT * 2.5)
MAX_TIME = 30
BONIFICATION_TEMPS = 5

clics_cartes = []
lclics_cartes = []
timer = None
essais = MAX_ESSAIS
temps_restant = MAX_TIME
temporisateur = None


def charger_image(numero):
    """Charger une image en se basant sur son numéro. Le numéro d'une image est une valeur entière de 0 à 8."""
    curdir = os.path.dirname(__file__)
    image_path = os.path.join(curdir, 'images/image_%02d.jpg' % (numero,))
    return ImageTk.PhotoImage(Image.open(image_path))


def charger_toutes_images():
    """Charger toutes les images dans une liste. Cette fonction renvoie une liste de 9 images."""
    # Déclarer une liste vide
    imgs = []

    # Charger les images une par une
    # Utiliser la fonction charger_image
    for i in range(IMAGES_COUNT + 1):
        img = charger_image(i)
        imgs.append(img)

    # Retourner la liste des images
    return imgs


def init_cartes_jeu():
    """Mélanger les cartes du jeu."""
    # Déclarer une liste vide
    img_pos = []

    # Remplir cette liste par les valeurs de 1 à 8
    # de la façon suivante : [1,1,2,2,3,3,...,8,8]
    for i in range(1, IMAGES_COUNT+1):
        for _ in range(2):
            img_pos.append(i)

    # Mélanger les cartes
    random.shuffle(img_pos)

    # Retourner la liste des cartes
    return img_pos


def init_cartes_devoiles():
    """Initialise la liste des cartes dévoilées."""
    # Déclarer une liste vide
    vis_imgs = []

    # Remplir la liste par des 0
    # car initialement aucune carte n'est dévoilée
    # On rappelle que le jeu contient 16 cartes
    for _ in range(IMAGES_COUNT * 2):
        vis_imgs.append(0)

    # Retourner la liste des cartes dévoilées.
    return vis_imgs


def creer_bouton(x, y, num_image):
    """Crée un bouton à la position indiquée : x, y. Initialement le bouton affiche l'image numéro num_image."""
    global fenetre, images_jeu
    btn = Button(fenetre, image=images_jeu[num_image],
                 command=partial(reveal_guess, x + NCOLS * y))
    btn.grid(row=y+1, column=x)
    return btn


def changer_image_bouton(num_bouton, num_image):
    """Permet de modifier l'image d'arrière plan du bouton num_bouton. L'image numéro num_image
    sera placée à la place de l'image existante. 
    num_bouton : est un nombre de 0 à 8
    num_image : est un nombre de 0 à 15"""
    global btns_jeu, images_jeu
    btns_jeu[num_bouton].configure(image=images_jeu[num_image])


def creer_boutons_jeu():
    """Créer les boutons de jeu sous forme d'une matrice 4x4. Les boutons crées sont retournés dans une matrice."""
    # Créer une liste vide
    btns = []

    # Créer 4x4 boutons qui ont l'image numéro 0 comme arrière plan
    # utiliser la fonction creer_bouton
    for j in range(NROWS):
        for i in range(NCOLS):
            btn = creer_bouton(i, j, 0)
            btns.append(btn)

    # retourner la liste des boutons
    return btns


def toutes_cartes_devoilees():
    """Déterminer si l'utilisateur a gagné le jeu. L'utilisateur gagne le jeu s'il arrive à dévoiler toutes les cartes.
    Cette fonction renvoie True si toutes les cartes ont été dévoilées."""
    global cartes_devoilees

    # Pour que les cartes soient dévoilées il faut que toutes
    # les cartes soient différentes de 0
    for img in cartes_devoilees:
        if img == 0:
            return False
    return True


def jeu_termine(gagne):
    """Lorsque le jeu est terminé on affiche un message convenable, puison demande à l'utilisateur s'il veut rejouer."""
    arreter_temporisateur()

    if gagne:
        title, msg = 'Bravo', 'Bravo, vous avez gagné.\nVoulez-vous rejouer ?'
    else:
        title, msg = 'Désolé', 'Vous avez perdu cette manche.\nVoulez-vous rejouer ?'

    res = messagebox.askyesno(title, msg)
    if res:
        rejouer()
    else:
        fenetre.destroy()


def reveal_guess(num_carte):
    global clics_cartes, lclics_cartes, cartes_devoilees, timer, essais, temps_restant

    # Si l'utilisateur veut cliquer une carte lorsque
    # les dernières images sont encore dévoilées
    if timer is not None:
        # On annule le timer, puis on cache les cartes dévoilées
        fenetre.after_cancel(timer)
        hide_guess()

    # Si la carte sélectionnée est déjà dévoilée on quitte la fonction
    if cartes_devoilees[num_carte] != 0:
        return

    # La carte sélectionnée n'est pas encore dévoilée :
    # On continue notre programme.
    l = len(clics_cartes)

    num_image = cartes_cachees[num_carte]
    if l == 0:
        # La première carte cliquée est automatiquement révélée
        clics_cartes.append((num_carte, num_image))
        changer_image_bouton(num_carte, num_image)
    elif l == 1:
        # Une seconde carte a été cliquée

        # On trouve le numero de la dernière carte cliquée
        lnum_carte, lnum_image = clics_cartes[-1]

        # L'utilisateur ne doit pas cliquer sur la même carte
        # une seconde fois
        if num_carte == lnum_carte:
            return

        # Si toutes les conditions précédentes ont été satisfaites
        # on révèle la carte cliquée
        clics_cartes.append((num_carte, num_image))
        changer_image_bouton(num_carte, num_image)

        if lnum_image == num_image:
            # Si les deux cartes cliquées correspondent
            # elles restent dévoilées
            cartes_devoilees[num_carte] = num_image
            cartes_devoilees[lnum_carte] = lnum_image

            # boniification de temps
            temps_restant += BONIFICATION_TEMPS
        else:
            # Si les cartes ne sont pas les mêmes elles
            # sont cachées après une seconde
            lclics_cartes = [cc for cc in clics_cartes]
            timer = fenetre.after(1000, hide_guess)
        # L'utilisateur est maintenant prêt pour un autre essai
        clics_cartes = []

        # On décrémente le nombre d'essais
        essais -= 1
        maj_nb_essais()

    if toutes_cartes_devoilees():
        jeu_termine(True)
    elif essais <= 0:
        jeu_termine(False)


def hide_guess():
    global lclics_cartes, timer
    timer = None
    changer_image_bouton(lclics_cartes[0][0], 0)
    changer_image_bouton(lclics_cartes[1][0], 0)
    lclics_cartes = []


def maj_nb_essais():
    global essais, lbl_nb_essais
    lbl_nb_essais.configure(
        text="Nombre d'essais restant : {}".format(essais))


def maj_temps_restant():
    global temps_restant, lbl_temps_restant, temporisateur
    lbl_temps_restant.configure(
        text="Temps restant : {} secondes".format(temps_restant))
    temps_restant -= 1
    if temps_restant < 0:
        jeu_termine(False)
    else:
        lancer_temporisateur()


def rejouer():
    global cartes_cachees, cartes_devoilees, btns_jeu, clics_cartes, essais, temps_restant, temporisateur

    arreter_temporisateur()

    essais = MAX_ESSAIS
    temps_restant = MAX_TIME
    clics_cartes = []
    cartes_devoilees = init_cartes_devoiles()
    cartes_cachees = init_cartes_jeu()

    maj_nb_essais()
    maj_temps_restant()

    for btn in btns_jeu:
        btn.configure(image=images_jeu[0])

    lancer_temporisateur()


def arreter_temporisateur():
    global temporisateur
    if temporisateur is not None:
        lbl_temps_restant.after_cancel(temporisateur)
        temporisateur = None


def lancer_temporisateur():
    global lbl_temps_restant, temporisateur
    temporisateur = lbl_temps_restant.after(1000, maj_temps_restant)


# Créer la fenêtre du jeu
fenetre = Tk()
fenetre.title('Memory Game')

lbl_nb_essais = Label(
    fenetre, text="Nombre d'essais restants : {}".format(essais))
lbl_nb_essais.grid(row=0, column=0)

lbl_temps_restant = Label(
    fenetre, text="Temps restant : {} secondes".format(temps_restant))
lbl_temps_restant.grid(row=0, column=1)

images_jeu = charger_toutes_images()
btns_jeu = creer_boutons_jeu()
cartes_cachees = init_cartes_jeu()
cartes_devoilees = init_cartes_devoiles()

lancer_temporisateur()

mainloop()
