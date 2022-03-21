from tkinter import *
from tkinter import messagebox
from tkinter import Entry
import random
root = Tk()
root.geometry("600x500")
Score = 0
count = ""

FPSBinds = ["w", "a", "s", "d", "space", "Button-1", "Double-Button-1", "Triple-Button-1"]
FPSBindsText = ["W", "A", "S", "D", "Spatie", "Enkele Klik", "Dubbele Klik", "Driedubbele klik"]


StartButton = Button(root, text="Start FPS Trainer", width=15)
ExitButton = Button(root, text="Exit FPS Trainer", width=15)
StartButton.pack(pady=30)
ExitButton.pack(pady=25)
TimerLabel = Label(root, text="Time Left: " + str(count), bd=1)
ScoreLabel = Label(root, text="Score: " + str(Score))
TimerLabel2 = Label(root, text="Time:")
TimerLabel2.pack()
textbox = Entry(root)
textbox.insert(0, "20")
textbox.pack()
print(count)

def SpelScherm():
    global ScoreLabel, TimerLabel, count
    count=int(textbox.get())
    TimerLabel2.destroy()
    textbox.destroy()
    StartButton.destroy()
    ExitButton.destroy()
    TimerLabel.pack(side=TOP)
    ScoreLabel.pack(side=TOP)
    countdown(count)
    Buttons()

def countdown(count):   
    global Score 
    TimerLabel.configure(text="Time Left: "  + str(count))
    if count > 0:
        root.after(1000, countdown, count-1)
    else:
        FPSLabel.destroy()
        MsgBox = messagebox.askquestion (message="gefeliciteerd, je hebt " + str(Score) + " punten gescoord! wil je opnieuw?")
        if MsgBox == 'yes':
            Score = 0
            SpelScherm()
        else:
            root.destroy()

def score(count):
    global Score
    FPSLabel.unbind("<" + FPSBinds[x] + ">")
    root.unbind("<" + FPSBinds[x] + ">")
    FPSLabel.destroy()  
    if x > 5:
        Score = Score + 2
    if x <= 5:
        Score = Score + 1
    ScoreLabel.configure(text="Score: " + str(Score))
    Buttons()

def Buttons():
    global FPSLabel, x
    x = random.randrange(0,8)
    FPSLabel = Label(root, text = FPSBindsText[x], relief=RAISED )
    if x > 5:
        FPSLabel.bind("<" + FPSBinds[x] + ">", score)
    elif x <= 5:
        root.bind("<" + FPSBinds[x] + ">", score)
    FPSLabel.place(x=random.randrange(0,500),y=random.randrange(0,400))

StartButton.config(command=SpelScherm)
ExitButton.config(command=root.destroy)

root.mainloop()