import streamlit as st
from pathlib import Path
import os

st.title("CRUD File Manager")


def show_items():
    items = list(Path().glob('*'))

    if items:
        st.subheader("Files & Folders")
        for item in items:
            st.write(item)


show_items()

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)


# CREATE FILE
if menu == "Create File":

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("FILE ALREADY EXISTS")

        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("FILE CREATED")


# READ FILE
elif menu == "Read File":

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, 'r') as file:
                st.text(file.read())

        else:
            st.error("FILE NOT FOUND")


# UPDATE FILE
elif menu == "Update File":

    file_name = st.text_input("Enter file name")

    option = st.radio(
        "Select Update Type",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            mode = "w" if option == "Overwrite" else "a"

            with open(file_name, mode) as file:
                file.write(content)

            st.success("FILE UPDATED")

        else:
            st.error("FILE NOT FOUND")


# DELETE FILE
elif menu == "Delete File":

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)

            st.success("FILE DELETED")

        else:
            st.error("FILE NOT FOUND")


# RENAME FILE
elif menu == "Rename File":

    old_name = st.text_input("Enter old file name")
    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)

            st.success("FILE RENAMED")

        else:
            st.error("FILE NOT FOUND")


# CREATE FOLDER
elif menu == "Create Folder":

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.error("FOLDER ALREADY EXISTS")

        else:
            p.mkdir()

            st.success("FOLDER CREATED")


# DELETE FOLDER
elif menu == "Delete Folder":

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            p.rmdir()

            st.success("FOLDER DELETED")

        else:
            st.error("FOLDER NOT FOUND")