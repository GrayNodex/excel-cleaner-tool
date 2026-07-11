from tkinter import *
from tkinter import ttk

def get_input():
 t = Tk()
 E1 = Entry()
 E1.pack()

 return E1

def show_input(input):
    ttk.Label(frm, text=input).grid(column=0, row=0)

    return input

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
input = get_input()

show_input(input)



ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()