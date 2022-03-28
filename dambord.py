from tkinter import *
root = Tk()
x = 0
y = 1
row = 1
root.columnconfigure(index=10,weight=10)
root.rowconfigure(index=10,weight=10)

def LabelMaker(x,y):
    global row
    for i in range(5):
        LabelsBlack = Label(bg="black",height=4, width=9)
        LabelsBlack.grid(column = x, row = row)
        x=x+2
    for i in range(5):
        LabelsWhite = Label(height=4, width=9)
        LabelsWhite.grid(column = y, row = row)
        y=y+2
    RowChecker()

def RowChecker():
    global row
    if row < 10:
        row = row + 1
        if row % 2 == 0:
            x= 1
            y=0
        else:
            x=0
            y=1
        LabelMaker(x,y)

LabelMaker(x,y)

root.mainloop()