from tkinter import Button
from tkinter import Tk
from tkinter import filedialog

# Choose a file
def choose_file():
    # Select a file from the file dialog.
    file_name = filedialog.askopenfilename()

    print(type(file_name))
    print(repr(file_name))

    # Stop the process because the user did not select a file.

    if isinstance(file_name, tuple):
        if not file_name:
            print("No file was chosen.")
            # Return None if the user cancels file selection.
            return None
    # Stop the process because the user did not select a file.
    elif file_name == '':
        print("No file was chosen.")
        # Return None if the user cancels file selection.
        return None
    
    # # Check whether the file format is valid.
    if not file_name:
        while  not file_name.endswith(".xlsx"):
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
