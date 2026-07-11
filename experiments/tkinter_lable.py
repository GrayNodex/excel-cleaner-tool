from tkinter import Tk, Toplevel
from tkinter import ttk



def show_message():
    new_win = Toplevel(root)
    new_win.title("Second")
    new_win.geometry("200x200")
    frm = ttk.Frame(new_win, padding=10)
    frm.grid()

    if 1 != 1:
        # root = Tk()
        # frm = ttk.Frame(root, padding=10)
        # frm.grid()
        ttk.Label(frm, text="Wrong").grid(column=0, row=0)
    elif 1 == 1:
        # root = Tk()
        # frm = ttk.Frame(root, padding=10)
        # frm.grid()
        print("creating label")
        ttk.Label(frm, text="Right").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=new_win.destroy).grid(column=0, row=10)


root = Tk()
root.title("Main")
frm = ttk.Frame(root, padding=10)
frm.grid()



ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
ttk.Button(frm, text="next", command=show_message).grid(column=1, row=0)
root.mainloop()