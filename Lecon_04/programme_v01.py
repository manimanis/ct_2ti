from tkinter import *

# Constantes Globales
XCELLS, YCELLS = 12, 20     # Nombre de cellules dans la grille
WCELL, HCELL = 25, 25       # Dimensions d'une cellule (pixels)
WGRILLE = WCELL * XCELLS    # Largeur de la Grille (pixels)
HGRILLE = HCELL * YCELLS    # Hauteur de la Grille (pixels)
XGRILLE, YGRILLE = 10, 10   # Position de la Grille (pixels)
WCANVAS = WGRILLE + XGRILLE * 2  # Largeur du Canvas
HCANVAS = HGRILLE + YGRILLE * 2  # Hauteur du Canvas

# Couleurs possibles des cellules
COLORS = ["#2196f3", "#f44336", "#e91e63",
          "#9c27b0", "#673ab7", "#03a9f4", "#009688"]

# Créer la fenêtre
window = Tk()

# Créer le Canvas de la grille du jeu
gcanvas = Canvas(window, width=WCANVAS, height=HCANVAS)
gcanvas.pack()

# Dessiner les bords de la grille
gcanvas.create_rectangle(4, 4, WCANVAS - 2, HCANVAS - 2, width=4)
gcanvas.create_rectangle(XGRILLE, XGRILLE,
                         WCANVAS - XGRILLE+2, HCANVAS - XGRILLE+2, width=2, outline="#999999")

# Initialiser la grille
for i in range(XCELLS):
    for j in range(YCELLS):
        gcanvas.create_rectangle(XGRILLE + WCELL * i, YGRILLE + HCELL * j,
                                 XGRILLE + WCELL * (i+1), YGRILLE + HCELL * (j+1), fill="#586241")

mainloop()
