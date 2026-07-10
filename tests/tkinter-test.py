from tkinter import Button
from tkinter import Tk
from tkinter import filedialog

def choose_file():
    file_name = filedialog.askopenfilename()

    print(type(file_name))
    print(repr(file_name))

    if isinstance(file_name, tuple):
        if not file_name:
            print("No file was chosen.")
            return None
    elif file_name == '':
        print("No file was chosen.")
        return None
    
    
    while  not file_name.endswith(".xlsx") and not file_name:
        print("Wrong file extentions.\nPlease choose again.")
        file_name = choose_file()

    return file_name


root = Tk()

button1 = Button(
    root,
    text="choose file",
    command=choose_file
)

button1.pack()


button2 = Button(
    root,
    text="exit",
    command=root.destroy
)

button2.pack()

root.mainloop()
