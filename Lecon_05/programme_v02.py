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
w.create_oval(ESPACEMENT, ESPACEMENT,
              ESPACEMENT + D_FEU, ESPACEMENT + D_FEU, fill='red', width=3)
w.create_oval(ESPACEMENT, 2 * ESPACEMENT + D_FEU,
              ESPACEMENT + D_FEU, 2*(ESPACEMENT + D_FEU), fill='yellow', width=3)
w.create_oval(ESPACEMENT, 3 * ESPACEMENT + 2 * D_FEU,
              ESPACEMENT + D_FEU, 3*(ESPACEMENT + D_FEU), fill='green', width=3)

mainloop()
