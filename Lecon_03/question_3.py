from tkinter import *

# Créer la fenêtre
w = Tk()

# Créer l'espace de dessin
c = Canvas(w, width=454, height=354)
c.pack()

# Dessiner la cheminée
c.create_rectangle(318, 2, 356, 60, fill="#800000")

# Dessiner le toit
c.create_polygon(2, 102, 452, 102, 227, 2, fill="#ffa500", outline="#000")

# Dessiner le mur
c.create_rectangle(27, 102, 427, 352, fill="#ffd700")

# Dessiner la fenêtre du toit
c.create_oval(202, 27, 252, 77, fill="#5f9ea0", width="2")
c.create_line(202, 52, 252, 52, width="5")
c.create_line(227, 27, 227, 77, width="5")

# Dessiner la porte
c.create_rectangle(72, 190, 173, 352, fill="#ffa500")

# Dessiner les fenêtres
c.create_rectangle(188, 190, 282, 284, fill="#afeeee", width="3")
c.create_line(235, 190, 235, 284, width="5")

c.create_rectangle(300, 190, 394, 284, fill="#afeeee", width="3")
c.create_line(347, 190, 347, 284, width="5")

mainloop()
