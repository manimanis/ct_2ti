from tkinter import *
import random


def init_grille():
    """Créer les cellules de la grille du jeu et initialiser la grille."""
    for j in range(YCELLS):
        rect_ids = []
        v_line = []
        for i in range(XCELLS):
            cell = gcanvas.create_rectangle(
                XGRILLE + i * WCELL, YGRILLE + j * HCELL,
                XGRILLE + (i+1) * WCELL, YGRILLE + (j+1) * HCELL,
                fill="black", state=HIDDEN)
            rect_ids.append(cell)
            v_line.append(None)
        cells_ids.append(rect_ids)
        cells_visibility.append(v_line)


def allumer_cell(x, y, color):
    """Permet d'allumer la cellule (x, y) en utilisant une des couleurs prédéfinies."""
    cells_visibility[y][x] = color
    gcanvas.itemconfigure(cells_ids[y][x], fill=COLORS[color], state=NORMAL)


def eteindre_cell(x, y):
    """Permet d'éteindre la cellule (x, y)."""
    if is_visible_cell(x, y):
        cells_visibility[y][x] = None
        gcanvas.itemconfigure(cells_ids[y][x], state=HIDDEN)


def is_visible_cell(x, y):
    """Permet de tester la visibilité d'une cellule."""
    return cells_visibility[y][x] is not None


def reset_grille():
    """Réinitialiser la grille sans recréer les cellules."""
    for j in range(YCELLS):
        for i in range(XCELLS):
            eteindre_cell(i, j)


def timer_event():
    """Tester le bon fonctionnement de la grille. Afficher des cellules d'une façon aléatoire."""
    global timer_id

    x, y = random.randrange(0, XCELLS), random.randrange(0, YCELLS)
    if not is_visible_cell(x, y):
        color = random.randrange(0, len(COLORS))
        allumer_cell(x, y, color)
    else:
        eteindre_cell(x, y)
    timer_id = window.after(10, timer_event)


def key_events(event):
    """Réagir au clavier."""
    global timer_id
    # print(dir(event))
    #print(chr(event.keycode), event.keysym, event.keysym_num)
    if chr(event.keycode) == 'R':
        reset_grille()
    elif chr(event.keycode) == 'Q':
        window.destroy()
    elif chr(event.keycode) == 'P':
        if timer_id is None:
            timer_id = window.after(10, timer_event)
        else:
            window.after_cancel(timer_id)
            timer_id = None


# Constantes Globales
XCELLS, YCELLS = 12, 20
WCELL, HCELL = 25, 25
WGRILLE, HGRILLE = WCELL * XCELLS, HCELL * YCELLS
XGRILLE, YGRILLE = 10, 10
WCANVAS, HCANVAS = WGRILLE + XGRILLE * 2, HGRILLE + YGRILLE * 2
COLORS = ["#2196f3", "#f44336", "#e91e63",
          "#9c27b0", "#673ab7", "#03a9f4", "#009688"]

# Créer la fenêtre
window = Tk()

# Créer le Canvas de la grille du jeu
gcanvas = Canvas(window, width=WCANVAS, height=HCANVAS)
gcanvas.pack()

# Dessiner les bords de la grille
gcanvas.create_rectangle(4, 4, WCANVAS - 2, HCANVAS - 2, width=2)
gcanvas.create_rectangle(XGRILLE, XGRILLE,
                         WCANVAS - XGRILLE+2, HCANVAS - XGRILLE+2, width=2, outline="#999999")

cells_ids = []          # ids, données par tkinter, des cellules de la grille
cells_visibility = []   # couleur des cellules: None = cellule invisible
init_grille()

# Réagir au clavier
window.bind('<Key>', key_events)

# Lancer le timer
timer_id = window.after(10, timer_event)

mainloop()
