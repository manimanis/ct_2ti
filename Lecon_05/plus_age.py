from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('Le plus agé')

opts = {'ipadx': 5, 'ipady': 5, 'padx': 5, 'pady': 5, 'sticky': 'nswe'}

label = Label(win, text='Nom du premier élève')
label.grid(row=0, column=0, **opts)

txt_name1_var = StringVar()
txt_name1 = Entry(win, width=32, textvariable=txt_name1_var)
txt_name1.grid(row=1, column=0, **opts)

label = Label(win, text='Nom du second élève')
label.grid(row=0, column=1, **opts)

txt_name2_var = StringVar()
txt_name2 = Entry(win, width=32, textvariable=txt_name2_var)
txt_name2.grid(row=1, column=1, **opts)

label = Label(win, text='Age')
label.grid(row=2, column=0, **opts)

txt_age1_var = IntVar()
txt_age1 = Entry(win, width=32, textvariable=txt_age1_var)
txt_age1.grid(row=3, column=0, **opts)

label = Label(win, text='Age')
label.grid(row=2, column=1, **opts)

txt_age2_var = IntVar()
txt_age2 = Entry(win, width=32, textvariable=txt_age2_var)
txt_age2.grid(row=3, column=1, **opts)


def btn_clicked():
    name1 = txt_name1_var.get()
    name2 = txt_name2_var.get()
    age1 = txt_age1_var.get()
    age2 = txt_age2_var.get()

    if age1 > age2:
        messagebox.showinfo(
            'Information', '{} est plus agé que {}'.format(name1, name2))
    elif age2 > age1:
        messagebox.showinfo(
            'Information', '{} est plus agé que {}'.format(name2, name1))
    else:
        messagebox.showinfo(
            'Information', '{} et {} ont le même age'.format(name1, name2))


btn = Button(win, text="Comparer", command=btn_clicked)
btn.grid(row=4, column=0, columnspan=2, **opts)

mainloop()
