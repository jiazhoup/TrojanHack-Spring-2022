
import sys
from unittest.mock import DEFAULT
import organizer
import node_parser
import tokenizer
import tkinter as tk
from PIL import Image, ImageTk

DEFAULT_POLICY_PATH = "default_policy"

def organize():
    # fileName = sys.argv[1]

    fileName = e.get()  # Get file name from text entry

    if fileName == None:
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
    Organize desktop using node structure
    """
    organizer.organizeDesktop(rootNode)



"""
Window object 
"""
root = tk.Tk()
root.geometry("300x400")


"""
Background
"""
bg_color = '#66FFB2'
root.configure(background=bg_color)


"""
Organize button. Calls the organize function
"""
btn_img = Image.open('Images/Mamluk Sultanate.png')
btn_img.thumbnail((100, 100))   # Rescale image
btn_img = ImageTk.PhotoImage(btn_img)
btn_label = tk.Label(image=btn_img)

btn = tk.Button(root, image=btn_img, command=organize, bd=0, bg=bg_color)
btn.pack(pady=(120, 0))


"""
Text entry
"""
e = tk.Entry(root, width=25, fg='gray', bd=0, bg='#f2f2f2', font='consolas 8')
e.pack(pady=(20, 0))
e.insert(0, 'Enter policy file name')


root.mainloop()
