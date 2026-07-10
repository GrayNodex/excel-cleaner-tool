from tkinter import filedialog
from tkinter import Tk


root = Tk()
root.withdraw()

while True:
    file_name = filedialog.askopenfilename()

    print("value:", repr(file_name))
    print("type:", type(file_name))
