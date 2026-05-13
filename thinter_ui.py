from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os

root = Tk()

root.title("CRUD File Manager")
root.geometry("500x500")


# FUNCTIONS

def create_file():

    file_name = entry1.get()
    content = text.get("1.0", END)

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "FILE ALREADY EXISTS")

    else:
        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "FILE CREATED")


def read_file():

    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'r') as file:

            text.delete("1.0", END)
            text.insert(END, file.read())

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def update_file():

    file_name = entry1.get()
    content = text.get("1.0", END)

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "FILE UPDATED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def delete_file():

    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():

        os.remove(p)

        messagebox.showinfo("Success", "FILE DELETED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def rename_file():

    old_name = entry1.get()
    new_name = entry2.get()

    p = Path(old_name)

    if p.exists():

        p.rename(new_name)

        messagebox.showinfo("Success", "FILE RENAMED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def create_folder():

    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():
        messagebox.showerror("Error", "FOLDER ALREADY EXISTS")

    else:
        p.mkdir()

        messagebox.showinfo("Success", "FOLDER CREATED")


def delete_folder():

    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():

        p.rmdir()

        messagebox.showinfo("Success", "FOLDER DELETED")

    else:
        messagebox.showerror("Error", "FOLDER NOT FOUND")


# UI

Label(root, text="Enter File/Folder Name").pack()

entry1 = Entry(root, width=50)
entry1.pack()

Label(root, text="Enter New Name (For Rename)").pack()

entry2 = Entry(root, width=50)
entry2.pack()

Label(root, text="Enter Content").pack()

text = Text(root, height=10, width=50)
text.pack()


Button(root, text="Create File", command=create_file).pack(pady=5)

Button(root, text="Read File", command=read_file).pack(pady=5)

Button(root, text="Update File", command=update_file).pack(pady=5)

Button(root, text="Delete File", command=delete_file).pack(pady=5)

Button(root, text="Rename File", command=rename_file).pack(pady=5)

Button(root, text="Create Folder", command=create_folder).pack(pady=5)

Button(root, text="Delete Folder", command=delete_folder).pack(pady=5)


root.mainloop()