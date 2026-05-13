# project - CURD 

from pathlib import Path
import os
def readfileandfolder() :
    p = Path ('')
    items = list(p.glob('*'))
    for index, file in enumerate(items):
        print (f'{index}-{file}')

def create_file():
    try:
        readfileandfolder()
        #c:\Users\HP\OneDrive\Desktop\file handelling>\hello.txt
        file_name = input('Enter name of your file')
        p = Path(file_name)
        if p.exists():
         print('FILE ALREADY EXISTS')
        else:
            with open(file_name, 'w') as file:
                content = input('Enter your file content')
                file.write (content)
                print ("FILE ADDED")
    except Exception as e:
        print (e)


def read_file():
    try:
        readfileandfolder()
        file_name = input("enter name of your file")
        p = Path(file_name)
        if p.exists():
          with open(file_name,"r") as file:
            print(file.read())
        else:
            print ('FILE NOT FOUND')
    except Exception as e:
        print (e)


def update_file():
    try:
        readfileandfolder()
        file_name = input('enter name of your file')
        p= Path(file_name)
        if p.exists():
            print ('press 1 to overwrite the content')
            print ('print 2 to append new content')
            
            option = int(input('enter your choice for updating a file'))
            if option == 1:
                with open (file_name, 'w') as file:
                    content = input ('enter your content')
                    file.write(content)
                    print ("CONTENT OVERWRITE")
            elif option ==2:
                with open (file_name, 'A') as file:
                    content = input ('enter your content')
                    file.write(content)
                    print ("CONTENT OVERWRITE")
            else:
                print ('INVALID INPUT')
        else:
            print ('FILE DOES NOT EXISTS')
    except Exception as e:
        print (e)
def delete_file():
    try:
        readfileandfolder()
        file_name = input ('enter name of your file')
        p = Path (file_name)
        if p.exists():
            os.remove (p) # OS is removing path of thet file
            # completely from the system
            print ('FILE DELETED')
        else:
            print ('FILE DELETED')
    except Exception as e:
        print (e)

def rename_file():
    readfileandfolder()
    file_name = input ("Enter name of your file")
    p = Path (file_name)
    if p.exists():
        new_file = input ("Enter new name of your file")
        p.rename(new_file)
        print ("FILE RENAMED")
    else:
        print ("FILE NOT FOUND")

def create_folder():
    readfileandfolder()
    folder_name = input ('enter name of your folder')
    p = Path (folder_name)
    if p.exists():
        print ("FOLDER ALREADY EXISTS")
    else:
        p.mkdir()
        print ('FOLDER CREATED')

def delete_folder():
    readfileandfolder()
    folder_name = input ('enter name of your folder')
    p = Path (folder_name)
    if p.exists():
        p.rmdir()
        print ('FOLDER DELETED')
    else:
        print ('FOLDER NOT FOUND')

def create_file_in_folder():
    folder_name = input ('ENTER name of your folder')
    file_name = input ('Enter name of your file')
    p = Path(folder_name/file_name)
    if p.exists():
        print ('FILE ALREADY EXISTS')
    else:
        print ()

while True:
    print ('press 1 for creating a file')
    print ('press 2 for reading a file')
    print ('press 3 for updating a file')
    print ('press 4 for deleting a file')
    print ('press 5 for renaming a file')
    print ('press 6 for creating a folder')
    print ('press 7 for delete the function')
    print ('press 0 for exiting..')

    option = int(input("enter your choice"))
    if option ==1:
        create_file ()
    if option==2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delete_file()
   
    if option == 5:
        rename_file()
    
    if option == 6:
        create_folder()
    
    if option == 7:
        delete_folder()
    
    if option == 0:
        break

    