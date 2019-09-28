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


def allumer_jaune():
    w.itemconfigure(rouge, fill='')
    w.itemconfigure(jaune, fill='yellow')
    w.after(1000, allumer_vert)


def allumer_vert():
    w.itemconfigure(jaune, fill='')
    w.itemconfigure(vert, fill='green')
    w.after(5000, allumer_rouge)


def allumer_rouge():
    w.itemconfigure(vert, fill='')
    w.itemconfigure(rouge, fill='red')
    w.after(5000, allumer_jaune)


allumer_rouge()
w.after(5000, allumer_jaune)

mainloop()
