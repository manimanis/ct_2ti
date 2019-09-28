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
                      ESPACEMENT + D_FEU, ESPACEMENT + D_FEU, fill='red', width=3)
jaune = w.create_oval(ESPACEMENT, 2 * ESPACEMENT + D_FEU,
                      ESPACEMENT + D_FEU, 2*(ESPACEMENT + D_FEU), fill='yellow', width=3)
vert = w.create_oval(ESPACEMENT, 3 * ESPACEMENT + 2 * D_FEU,
                     ESPACEMENT + D_FEU, 3*(ESPACEMENT + D_FEU), fill='green', width=3)


def clignoter():
    global w

    # faire clignoter le rouge
    fill = w.itemcget(rouge, 'fill')
    if fill != '':
        w.itemconfigure(rouge, fill='')
    else:
        w.itemconfigure(rouge, fill='red')

    # faire clignoter le jaune
    fill = w.itemcget(jaune, 'fill')
    if fill != '':
        w.itemconfigure(jaune, fill='')
    else:
        w.itemconfigure(jaune, fill='yellow')

    # faire clignoter le jaune
    fill = w.itemcget(vert, 'fill')
    if fill != '':
        w.itemconfigure(vert, fill='')
    else:
        w.itemconfigure(vert, fill='green')

    w.after(1000, clignoter)


w.after(1000, clignoter)

mainloop()
