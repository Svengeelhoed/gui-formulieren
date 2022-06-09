from tkinter import *
from tkinter import messagebox
import string
import random
from random import shuffle

root = Tk()
root.title("Raad het woord")
root.geometry("250x400")
root.AantalPunten = 0

AlphabetList = list(string. ascii_lowercase)
SvList = []
WoordAntwoord = []
AantalLetters = 0
SpinboxList = []
GoButton = Button(root, text="Go", width = 10)
WoordEntry = Entry(root, width = 10)
DoneButton = Button(root, text="Done", width= 10)
WoordEntry.pack(pady=40)
GoButton.pack(pady=40)

# def Start():
#     alphabetlist = list(string. ascii_lowercase)
#     sv_list = []
#     WoordAntwoord = []
#     AantalPunten = 0

#     WoordEntry.pack(pady=40)
#     GoButton.pack(pady=40)

def GoButtonFunc():
    global HetWoordList,AantalLetters,PuntenLabel,Spinboxes,SpinboxValues,WoordEntryStr
    HetWoordList = list(WoordEntry.get())
    root.HetWoordStr = WoordEntry.get()
    root.AantalPunten = len(HetWoordList) * len(HetWoordList)
    PuntenLabel = Label(text="Punten: " + str(root.AantalPunten))
    PuntenLabel.pack()
    for i in range(len(HetWoordList)):
        SvList.append(StringVar(root))
    if len(WoordEntry.get()) >= 4 and len(WoordEntry.get()) <= 9:
        for i in range(len(WoordEntry.get())):
            SpinboxValues = list(HetWoordList[i])
            for e in range(4):
                SpinboxValues.append(random.choice(AlphabetList))
            shuffle(SpinboxValues)
            Spinboxes = Spinbox(root, values=SpinboxValues, textvariable=SvList[i])
            SpinboxList.append(Spinboxes)
            Spinboxes.pack(pady=10)
        DoneButton.pack(pady=20)
        AantalLetters = WoordEntry.get()
        WoordEntry.destroy()
        GoButton.destroy()
    else:
        messagebox.showinfo(message="Je hebt niet genoeg of teveel letters in je woord, probeer opnieuw. Je woord moet tussen de 4 en 7 letters hebben.")
    

def DoneButtonFunc():
    WoordAntwoord = []
    AantalGoed = 0
    for i in range(len(HetWoordList)):
        WoordAntwoord.append(SvList[i].get())
        if WoordAntwoord[i] == HetWoordList[i]:
            AantalGoed += 1
        else:
            root.AantalPunten -= 2
            PuntenLabel.configure(text="Punten: " + str(root.AantalPunten))
    if AantalGoed < len(HetWoordList):
        AantalFout = len(HetWoordList) - AantalGoed
        messagebox.showinfo(message="Helaas, je hebt " + str(AantalFout) + " letters fout!")
    if AantalGoed == len(HetWoordList):
        messagebox.showinfo(message="gefeliciteerd, je hebt het woord geraden!")
        root.after(2000)
        root.destroy()
    if root.AantalPunten < 0:
        messagebox.showinfo(message="helaas, je hebt verloren. Het woord was " + root.HetWoordStr)
        root.after(2000)
        root.destroy()
    WoordAntwoord = []


GoButton.configure(command=GoButtonFunc)
DoneButton.configure(command=DoneButtonFunc)


root.mainloop()