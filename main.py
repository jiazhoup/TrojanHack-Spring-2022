import sys
from unittest.mock import DEFAULT
import os
import pickle
import organizer
import node_parser
import tokenizer
import tkinter as tk
from PIL import Image, ImageTk

DEFAULT_POLICY_PATH = "default_policy.txt"


def organize():
    # fileName = sys.argv[1]

    fileName = e.get()  # Get file name from text entry

    if fileName == 'Enter policy file name':
        fileName = DEFAULT_POLICY_PATH

    """
    Read policy file, convert to string
    """
    data = None
    try:
        with open(fileName, 'r') as f:
            data = f.read().rstrip()
    except FileNotFoundError:
        print("Error. File not found.")
        quit()

    """
    Use parser to create node structure
    """
    rootNode = node_parser.tokensToNode(tokenizer.tokenize(data))

    """
    Organize desktop using node structure, return move history
    """
    moveHistory = organizer.organizeDesktop(rootNode)

    with open("moveHistory", "wb") as fp:  # Pickling
        pickle.dump(moveHistory, fp)


"""
Unpickle the file containing moveHistory. 
"""
def keepChanges():
    with open('moveHistory', 'rb') as fp:  # Unpickling
        moveHistory = pickle.load(fp)

    for move in moveHistory:  # Move the files back to the desktop
        os.rename(move[1], move[0])

    os.remove('moveHistory')


"""
Window object 
"""
root = tk.Tk()
root.geometry("300x400")
root.iconbitmap('Images/file_archive_folders_icon_193943.ico')
root.title('Bro-ganizer')


"""
Background
"""
bg_color = '#484848'
root.configure(background=bg_color)


"""
Logo?
"""
logo = Image.open('Images/cool_guy.jpg')
logo.thumbnail((180, 180))  # Rescale image
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo)
tk.Button(root, image=logo).pack(side='top', pady=(100, 0))

"""
Text entry
"""
e = tk.Entry(root, width=25, fg='gray', bd=0, bg='#f2f2f2', font='consolas 8')
e.pack(pady=(40, 0))
e.insert(0, 'Enter policy file name')


"""
Revert button. Calls keepChanges function
"""
btn_img2 = Image.open('Images/goback.png')
btn_img2.thumbnail((55, 55))  # Rescale image
btn_img2 = ImageTk.PhotoImage(btn_img2)
btn_label2 = tk.Label(image=btn_img2)

btn2 = tk.Button(root, image=btn_img2, command=keepChanges, bd=0, bg=bg_color)
btn2.pack(padx=(73, 0),
          pady=(10, 0),
          expand=False,
          fill='x',
          side='left',
          anchor='ne')


"""
Organize button. Calls the organize function
"""
btn_img = Image.open('Images/change.png')
btn_img.thumbnail((55, 55))  # Rescale image
btn_img = ImageTk.PhotoImage(btn_img)
btn_label = tk.Label(image=btn_img)

btn = tk.Button(root, image=btn_img, command=organize, bd=0, bg=bg_color)
btn.pack(padx=40,
         pady=10,
         expand=False,
         fill='x',
         side='left',
         anchor='n')

root.mainloop()
