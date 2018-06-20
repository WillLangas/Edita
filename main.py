#!/usr/bin/env python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    from tkinter import filedialog
except ImportError:
    import tkFileDialog

import datetime

try:
    from tkinter import messagebox
except ImportError:
    import tkMessageBox

try:
    import tkinter.colorchooser
except ImportError:
    from tkColorChooser import askcolor

filename = None

def clearAll():
    text.delete(0.0,END)

def newFile():
    global filename
    filename = "Untitled"
    clearAll()

def saveFile():
    global filename
    t = text.get(0.0,END)
    f = open(filename, 'w') #Writes a file
    f.write(t)
    f.close()

def saveAs():
    fil = asksaveasfile(mode='w', defaultextension='.txt') #Saves file
    t = text.get(0.0, END)
    try:
        fil.write(t.rstrip())
    except:
        showerror(title="Rats!", message="Unable to save file...") #Exception handling

def openFile():
    f = askopenfile(mode='r') #Read mode of a file, opens any file
    t = f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

def kill():
    root.destroy()

def insertDate():
    date = datetime.date.today()
    text.insert(INSERT, date)

def insertLine():
    line = "_" * 50
    text.insert(INSERT,line)

def bold():
    text.config(font = ("Times",20,"bold"))

def italic():
    text.config(font = ("Times",20,"italic"))

def underline():
    text.config(font = ("Times",20,"underline"))

def normal():
    text.config(font = ("Times",20))

def color():
    (triple,color) = askcolor()
    if color:
        text.config(background=color)

def textColor():
    (triple,color) = askcolor()
    if color:
        text.config(foreground=color)

def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def paste():
    try:
        text = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT,text)
    except:
        tkMessageBox.showerror(title = "Rats!", label="Pasting Error")

root = Tk()
root.title("Edita Notepad 1.0")
menu = Menu(root)
filemenu = Menu(root)
root.config(menu = menu)

menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=kill)

modmenu = Menu(root)
menu.add_cascade(label="Edit",menu=modmenu)
modmenu.add_command(label="Copy",command=copy)
modmenu.add_command(label="Paste",command=paste)
modmenu.add_separator()
modmenu.add_command(label="Clear",command=clearAll)

insmenu = Menu(root)
menu.add_cascade(label="Insert",menu=insmenu)
insmenu.add_command(label="Date",command=insertDate)
insmenu.add_command(label="Line",command=insertLine)

formatmenu = Menu(menu)
menu.add_cascade(label="Format",menu=formatmenu)
formatmenu.add_cascade(label="Color",command=textColor)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal',command=normal)
formatmenu.add_radiobutton(label='Bold',command=bold)
formatmenu.add_radiobutton(label='Underline',command=underline)
formatmenu.add_radiobutton(label='Italic',command=italic)

persomenu = Menu(root)
menu.add_cascade(label="Personalize",menu=persomenu)
persomenu.add_command(label="Background",command=color)

text = Text(root, height=30, width=50, font=("Times", 20))

scroll = Scrollbar(root, command=text.yview)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)

text.pack()
root.resizable(0,0)

root.mainloop()
