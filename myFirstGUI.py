"""This program will add whatever you type into a text file."""

from tkinter import *
from pathlib import Path
import sys

p = Path.cwd()


def submit():
    response = entry.get()
    with open("myFirstGuitext.txt", "a", encoding="UTF-8") as file_obj:
        file_obj.write(f"{response}\n")
        


def delete():
    entry.delete(0, END)


def deleteCurrentTextContents():
    with open("myFirstGuitext.txt", "w", encoding="UTF-8") as file_obj:
        file_obj.write("")


def quit():
    sys.exit()


window = Tk()
window.geometry("420x420")

entry = Entry(window, font=("Arial", 50))
entry.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

delete_text_contents_button = Button(window, text="Delete current contents of text", command=deleteCurrentTextContents)
delete_text_contents_button.pack()

quit_button = Button(window, text="quit", command=quit)
quit_button.pack()

window.mainloop()
