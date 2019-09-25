# import all the contents of the tkinter module
from tkinter import *

# create the application window
master = Tk()

# create a canvas to draw into
w = Canvas(master, width=880, height=100)

# make the application window the same size as the canvas
w.pack()

# forme 1
w.create_rectangle(5, 5, 35, 35, fill="#2196f3")
w.create_rectangle(5, 35, 35, 65, fill="#2196f3")
w.create_rectangle(35, 35, 65, 65, fill="#2196f3")
w.create_rectangle(35, 65, 65, 95, fill="#2196f3")

# forme 2
w.create_rectangle(130, 35, 160, 65, fill="#f44336")
w.create_rectangle(130, 65, 160, 95, fill="#f44336")
w.create_rectangle(160, 5, 190, 35, fill="#f44336")
w.create_rectangle(160, 35, 190, 65, fill="#f44336")

# forme 3
w.create_rectangle(255, 5, 285, 35, fill="#e91e63")
w.create_rectangle(255, 35, 285, 65, fill="#e91e63")
w.create_rectangle(255, 65, 285, 95, fill="#e91e63")
w.create_rectangle(285, 65, 315, 95, fill="#e91e63")

# forme 4
w.create_rectangle(380, 65, 410, 95, fill="#9c27b0")
w.create_rectangle(410, 5, 440, 35, fill="#9c27b0")
w.create_rectangle(410, 35, 440, 65, fill="#9c27b0")
w.create_rectangle(410, 65, 440, 95, fill="#9c27b0")

# forme 5
w.create_rectangle(535, 5, 565, 35, fill="#673ab7")
w.create_rectangle(505, 35, 535, 65, fill="#673ab7")
w.create_rectangle(535, 35, 565, 65, fill="#673ab7")
w.create_rectangle(565, 35, 595, 65, fill="#673ab7")

# forme 6
w.create_rectangle(630, 5, 660, 35, fill="#03a9f4")
w.create_rectangle(660, 5, 690, 35, fill="#03a9f4")
w.create_rectangle(630, 35, 660, 65, fill="#03a9f4")
w.create_rectangle(660, 35, 690, 65, fill="#03a9f4")

# forme 7
w.create_rectangle(755, 5, 785, 35, fill="#009688")
w.create_rectangle(785, 5, 815, 35, fill="#009688")
w.create_rectangle(815, 5, 845, 35, fill="#009688")
w.create_rectangle(845, 5, 875, 35, fill="#009688")

mainloop()
