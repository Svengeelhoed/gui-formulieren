import tkinter
from tkinter import *
root = tkinter.Tk()
root.geometry("250x250")
root.config(bg="grey")
GetalDisplay=0
laatstgeklikt = ""
checkbox_var = IntVar()

UpButton = tkinter.Button(root,text="Up", bg="white", width="30")
UpButton.pack(padx=10, pady=30)

GetalLabel = tkinter.Label(root, text=GetalDisplay, bg="white", width="30")
GetalLabel.pack()

DownButton = tkinter.Button(root,text="Down", bg="white", width="30")
DownButton.pack(padx=10, pady=30)

def buttonUp():
    global GetalDisplay, laatstgeklikt,state
    GetalDisplay = GetalDisplay + 1
    GetalLabel.config(text=GetalDisplay)
    if GetalDisplay >= 1:
        root.config(bg="green")
    if GetalDisplay == 0:
        root.config(bg="grey")
    GetalLabel.bind("<Double-Button-1>", DoubleClickUp)
    root.bind("<Double-space>", DoubleClickUp)
    laatstgeklikt = "Up"
    checkbutton1.config(state="normal")

def ButtonDown():
    global GetalDisplay, laatstgeklikt
    GetalDisplay = GetalDisplay - 1
    GetalLabel.config(text=GetalDisplay)
    if GetalDisplay < 0:
        root.config(bg="red")
    elif GetalDisplay == 0:
        root.config(bg="grey")
    GetalLabel.bind("<Double-Button-1>", DoubleClickDown)
    root.bind("<Double-space>", DoubleClickDown)
    laatstgeklikt = "Down"
    checkbutton1.config(state="normal")

def LeaveLabel(e):
    if GetalDisplay > 0:
        root.config(bg="green")
    if GetalDisplay < 0:
        root.config(bg="red")
    if GetalDisplay == 0:
        root.config(bg="grey")

def EnterLabel(e):
    root.config(bg="yellow")

def DoubleClickUp(e):
    global GetalDisplay, laatstgeklikt
    GetalDisplay = GetalDisplay * 3
    GetalLabel.config(text=GetalDisplay)
    laatstgeklikt = "dubbelup"

def DoubleClickDown(e):
    global GetalDisplay, laatstgeklikt
    GetalDisplay = GetalDisplay / 3
    GetalLabel.config(text=GetalDisplay)
    laatstgeklikt = "dubbeldown"

def ButtonBindsUp(e):
    buttonUp()

def ButtonBindsDown(e):
    ButtonDown()

def check():
    global GetalDisplay
    if checkbox_var.get() == 1:
        if laatstgeklikt == "Up":
            GetalDisplay = GetalDisplay + 1
        if laatstgeklikt == "Down":
            GetalDisplay = GetalDisplay - 1
        if laatstgeklikt == "dubbelup":
            GetalDisplay = GetalDisplay * 3
        if laatstgeklikt == "dubbeldown":
            GetalDisplay = GetalDisplay / 3
        GetalLabel.config(text=GetalDisplay)
        root.after(200,check)  

checkbutton1 = Checkbutton(root, text='Autoclicker', command=check, variable=checkbox_var, onvalue = 1,offvalue=0, state = 'disabled')
checkbutton1.pack()

UpButton.config(command=buttonUp)
DownButton.config(command=ButtonDown)

GetalLabel.bind("<Enter>", EnterLabel)
GetalLabel.bind("<Leave>", LeaveLabel)

root.bind("<Up>", ButtonBindsUp)
root.bind("<+>", ButtonBindsUp)
root.bind("<minus>", ButtonBindsDown)
root.bind("<Down>", ButtonBindsDown)

root.mainloop()