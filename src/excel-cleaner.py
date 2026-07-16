import os
import pandas as pd

from tkinter import Tk, Toplevel, filedialog
from tkinter import ttk


# ==============================
# Application State
# ==============================

selected_file = None


# ==============================
# File Selector Module
# ==============================

def choose_file():
    """
    Open file dialog and select an Excel file.

    Return:
        str: selected file path
        None: if selection fails
    """

    global selected_file

    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Excel files", "*.xlsx *.xls")
        ]
    )


    # User cancels selection
    if file_path == "":
        show_message(
            "No file was selected."
        )
        return None


    # Check extension
    if not file_path.endswith(
        (".xlsx", ".xls")
    ):
        show_message(
            "Invalid file format."
        )
        return None


    selected_file = file_path


    show_message(
        "File selected:\n"
        + selected_file
    )


    return selected_file



# ==============================
# File Cleaner Module
# ==============================

def clean_file():

    global selected_file


    # Check file selection
    if selected_file is None:
        show_message(
            "Please select a file first."
        )
        return None


    try:

        # Read Excel file
        df = pd.read_excel(
            selected_file
        )


        # Remove rows with empty values
        df = df.dropna()


        # Remove duplicated IDs
        if "id" in df.columns:
            df = df.drop_duplicates(
                subset=["id"],
                keep="first"
            )



        # Create output folder
        output_dir = os.path.expanduser(
            "~/output"
        )

        os.makedirs(
            output_dir,
            exist_ok=True
        )


        output_file = os.path.join(
            output_dir,
            "cleaned_file.xlsx"
        )


        # Save cleaned file
        df.to_excel(
            output_file,
            index=False
        )


        show_message(
            "Cleaning completed.\n\n"
            f"Saved to:\n{output_file}"
        )


        return df


    except Exception as e:

        show_message(
            f"Cleaning failed:\n{e}"
        )

        return None



# ==============================
# GUI Module
# ==============================

def show_message(message):

    window = Toplevel(root)

    window.title(
        "Message"
    )

    window.geometry(
        "400x200"
    )


    frame = ttk.Frame(
        window,
        padding=20
    )

    frame.grid()



    label = ttk.Label(
        frame,
        text=message,
        wraplength=350
    )

    label.grid(
        column=0,
        row=0,
        pady=10
    )


    button = ttk.Button(
        frame,
        text="OK",
        command=window.destroy
    )

    button.grid(
        column=0,
        row=1
    )



# ==============================
# Main Window
# ==============================

root = Tk()

root.title(
    "Excel Cleaner"
)

root.geometry(
    "500x150"
)



frame = ttk.Frame(
    root,
    padding=20
)

frame.grid()



select_button = ttk.Button(
    frame,
    text="Choose Excel File",
    command=choose_file
)

select_button.grid(
    column=0,
    row=0,
    padx=10
)



clean_button = ttk.Button(
    frame,
    text="Clean File",
    command=clean_file
)

clean_button.grid(
    column=1,
    row=0,
    padx=10
)



exit_button = ttk.Button(
    frame,
    text="Exit",
    command=root.destroy
)

exit_button.grid(
    column=2,
    row=0,
    padx=10
)



root.mainloop()