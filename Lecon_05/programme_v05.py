from tkinter import *

# Créer la fenêtre
win = Tk()

# Constantes
D_FEU = 80     # Diamètre d'un feu
ESPACEMENT = 20  # Espacement entre les feux
W_CANVAS = D_FEU + 2 * ESPACEMENT
H_CANVAS = 3 * D_FEU + 4 * ESPACEMENT

# Créer un Canvas
w = Canvas(win, width=W_CANVAS, height=H_CANVAS)
w.pack()

# Créer trois cercles de diamètre 100
rouge = w.create_oval(ESPACEMENT, ESPACEMENT,
                      ESPACEMENT + D_FEU, ESPACEMENT + D_FEU, fill='', width=3)
jaune = w.create_oval(ESPACEMENT, 2 * ESPACEMENT + D_FEU,
                      ESPACEMENT + D_FEU, 2*(ESPACEMENT + D_FEU), fill='', width=3)
vert = w.create_oval(ESPACEMENT, 3 * ESPACEMENT + 2 * D_FEU,
                     ESPACEMENT + D_FEU, 3*(ESPACEMENT + D_FEU), fill='', width=3)

compteur = 0
clignoteur_id = None


def allumer_jaune():
    w.itemconfigure(rouge, fill='')
    w.itemconfigure(jaune, fill='yellow')
    win.after(1000, allumer_vert)


def allumer_vert():
    global compteur, clignoteur_id
    w.itemconfigure(jaune, fill='')
    w.itemconfigure(vert, fill='green')
    compteur = 0
    clignoteur_id = win.after(5000, clignoter_jaune)


def allumer_rouge():
    w.itemconfigure(vert, fill='')
    w.itemconfigure(rouge, fill='red')
    win.after(5000, allumer_jaune)


def clignoter_jaune():
    global compteur, clignoteur_id
    win.after_cancel(clignoteur_id)
    if compteur < 6:
        etat = w.itemcget(jaune, 'fill')
        if etat == 'yellow':
            w.itemconfigure(jaune, fill='')
        else:
            w.itemconfigure(jaune, fill='yellow')
        compteur += 1
        clignoteur_id = win.after(500, clignoter_jaune)
    else:
        win.after(1000, allumer_rouge)


allumer_rouge()
win.after(5000, allumer_jaune)

mainloop()
