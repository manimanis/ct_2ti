# This code source is for educational purpose
#-------------------------------------------------

# import all the contents of the tkinter module
from tkinter import *

# create the application window
master = Tk()

# create a canvas to draw into
w = Canvas(master, width=200, height=100)

# make the application window the same size as the canvas
w.pack()

# draw a black line
w.create_line(0, 0, 200, 100)

# draw a red dashed line
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# draw a blue filled rectangle
w.create_rectangle(50, 25, 150, 75, fill="blue")

# make the window interactive
mainloop()