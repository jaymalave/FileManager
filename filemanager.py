from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb





def open_window():
    read = easygui.fileopenbox()

    return read

def open_file():
    string = open_window()

    try:
        os.startfile(string)

    except:
        mb.showinfo('File Manager Says', "File not found")

def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()

    shutil.copy(source1,destination1)

    mb.showinfo('File Manager Says', "File copied.")

def remove_folder():
    delFolder = filedialog.askdirectory()

    os.rmdir(delFolder)

    mb.showinfo('File Manager Says', "The Folder is deleted.")

def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
        mb.showinfo('File manager Says', "The file was deleted.")
    else:
        mb.showinfo('File Manager Says', "The file is was not found")

def move_file():
    source  = open_window()
    destination = filedialog.askdirectory()

    shutil.move(source, destination)
    mb.showinfo('File Manager Says', "The file is moved")

def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of the new folder")

    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)

    os.mkdir(path)
    mb.showinfo('The File Manager Says', "Folder created")

def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted!")

def list_files():
    folderList = filedialog.askdirectory()
    sortList = sorted(os.listdir(folderList))
    i=0
    print("Files in ", folderList, "folder are: ")
    while(i<len(sortList)):
        print(sortList[i]+'\n')
        i += 1


root = Tk()

Label(root, text="File Manager", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)
Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)
Button(root, text = "Copy a file", command = copy_file).grid(row = 25, column = 2)
Button(root, text = "Delete a folder", command =remove_folder).grid(row = 35, column = 2)
Button(root, text = "Delete a file", command =delete_file).grid(row = 45, column = 2)
Button(root, text = "Move a file", command =move_file).grid(row = 55, column = 2)
Button(root, text = "Make a folder", command =make_folder).grid(row = 65, column = 2)
Button(root, text = "Delete a folder", command =remove_folder).grid(row = 85, column = 2)
Button(root, text = "List a folder", command =list_files).grid(row = 95, column = 2)

root.mainloop();






