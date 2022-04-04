from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Entry, messagebox
from datetime import datetime
root = Tk()
TimeDiff = StringVar()
root.geometry("300x150")
root.title("Days by date calculator")
root.rowconfigure(index=3,weight=250)

DagList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
MaandList=["Jan","Feb","Mar","Apr","May", "Jun","Jul","Aug","Sep", "Okt","Nov","Dec"]
MaandNumList=[1,2,3,4,5,6,7,8,9,10,11,12]

DateString = Label(text="Date:",font=20)
ComboBoxMaand = Combobox(root, width=8)
ComboBoxDag = Combobox(root, width=8)
GoButton = Button(root, text="go")
dash1 = Label(text="-")
dash2 = Label(text="-")
DateString.place(x=125)
ComboBoxMaand.place(x=115, y= 60)
ComboBoxDag.place(x=20, y= 60)
JaarEntry=Entry(root, width=8)
JaarEntry.insert(END, str(datetime.now().strftime("%Y")))
JaarEntry.place(x=210, y=61)
GoButton.place(x = 140, y = 110)
dash1.place(x=98, y=60)
dash2.place(x=193, y=60)
ComboBoxDag["values"]=DagList
ComboBoxMaand["values"]=MaandList
ComboBoxDag.set(datetime.now().strftime("%d"))
ComboBoxMaand.set(datetime.now().strftime("%b"))

def GoButtonFunc():
    IngevuldeTijd= str(ComboBoxDag.get()) +"-"+ ComboBoxMaand.get() +"-"+ str(JaarEntry.get())
    # print(IngevuldeTijd)
    Tijd1 = datetime.strptime(IngevuldeTijd, "%d-%b-%Y").date()
    Tijd2 = datetime.now().date()
    # print(Tijd1)
    # print(Tijd2)
    TimeCalc(Tijd1, Tijd2)
    
def TimeCalc(Tijd1, Tijd2):    
    TimeDiff = (Tijd1 - Tijd2).days
    TimeDiffMessageBox(TimeDiff)

def TimeDiffMessageBox(TimeDiff):
    if int(TimeDiff) == 0:
        messagebox.showinfo(message="dit is vandaag")
    if int(TimeDiff) > 0:
        messagebox.showinfo(message="dit is " + str(TimeDiff) + " dagen in de toekomst")
    if int(TimeDiff) < 0:
        messagebox.showinfo(message="dit is " + str(TimeDiff) + " dagen geleden")
    
GoButton.config(command=GoButtonFunc)

root.mainloop()