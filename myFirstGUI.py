"""This program will add whatever you type into a text file."""

from tkinter import *
from pathlib import Path
import sys

p = Path.cwd()

NAME_OF_TEXT_FILE = "myFirstGuitext.txt"


def submit():
    response = entry.get()
    with open(
        NAME_OF_TEXT_FILE, "a", encoding="UTF-8"
    ) as file_obj:  # Writes contents to a text file.
        file_obj.write(f"{response}\n")
    entry.delete(0, END)

def delete():  # Deletes text from the text bar.
    entry.delete(0, END)


def deleteCurrentTextContents():  # Will remove contents from the current file.
    with open(NAME_OF_TEXT_FILE, "w", encoding="UTF-8") as file_obj:
        file_obj.write("")


def quit():
    sys.exit()


def showContentsOfText():
    textContentWindow = Tk()
    textContentWindow.title("Text File Contents")
    textContentWindow.geometry('240x240')
    
    with open(NAME_OF_TEXT_FILE, encoding="UTF-8") as file_obj:
        content = file_obj.read()

    contentArea = Label(textContentWindow, text=content)
    contentArea.pack()
    

window = Tk()
window.title("Enter word to be put inside a text file")

entry = Entry(window, font=("Arial", 50))
entry.pack()

submit_button = Button(window, font=("Arial", 30), text="submit", command=submit)
submit_button.pack()

delete_button = Button(window, font=("Arial", 30), text="delete", command=delete)
delete_button.pack()

show_contents_of_text_button = Button(window, font=("Arial", 30), text="show current contents of text", command=showContentsOfText)
show_contents_of_text_button.pack()

delete_text_contents_button = Button(window, font=("Arial", 30), text="Delete current contents of text", command=deleteCurrentTextContents)
delete_text_contents_button.pack()

quit_button = Button(window, font=("Arial", 30), text="quit", command=quit)
quit_button.pack()

window.mainloop()

# HELLO