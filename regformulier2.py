from tkinter import *
root = Tk()
root.title("Registratie Formulier Sportdag")
root.geometry("350x500")


StartLabel = Label(
    root, text="Welkom bij het registratieformulier van de sportdag. Vul de vragen zo eerlijk mogelijk in.")
StartButton = Button(
    root, text="Ga")
StartButton.pack()
StartLabel.pack()

Vraag1 = Label(root, text="Hoe oud ben je?", font=20)
Vraag2 = Label(root, text="Hoe lang ben je?", font=20)
Vraag3 = Label(root, text="Welke kaas vindt je het lekkerst?", font=20)
Vraag4 = Label(root, text="Mayonaise of Ketchup?", font=20)
Vraag5 = Label(root, text="Wat is je schoenmaat?", font=20)

Antwoorden1 = (("14", "14"),
               ("15", "15"),
               ("16", "16"),
               ("17", "17"),
               ("18", "18"))
Antwoorden2 = (("1,70", "1,70"),
               ("1,75", "1,75"),
               ("1,80", "1,80"),
               ("1,85", "1,85"),
               ("1,90", "1,90"))
Antwoorden3 = (("Jonge kaas", "Jonge kaas"),
               ("Oude Kaas", "Oude Kaas"),
               ("Schimmelkaas", "Schimmelkaas"),
               ("Heksenkaas", "Heksenkaas"),
               ("Geen kaas", "Geen kaas"))
Antwoorden4 = (("Mayonaise", "Mayonaise"),
               ("Ketchup", "Ketchup"))
Antwoorden5 = (("38", "38"),
               ("40", "40"),
               ("42", "42"),
               ("44", "44"),
               ("46", "46"))

Vragen = [Vraag1, Vraag2, Vraag3, Vraag4, Vraag5]
Antwoorden = [Antwoorden1, Antwoorden2, Antwoorden3, Antwoorden4, Antwoorden5]
AntwoordList = []
RadioList = []
AntwoordAmounts = ["4", "4", "4", '1', '4']
AntwoordLabels = []
x = -1
SelectedAntwoord = StringVar()


StartButton.pack()
StartLabel.pack()


def VraagFunc(x=x + 1):
    StartButton.destroy()
    StartLabel.destroy()
    if x == 5:
        AntDisplay()
    else:
        Vragen[x].pack()
        for Antwoord in Antwoorden[x]:
            r = Radiobutton(
                root, text=Antwoord[0], value=Antwoord[1], variable=SelectedAntwoord, font="20")
            RadioList.append(r)
            r.pack(pady=5, padx=50, anchor="w")
        GoButton = Button(
            root, text="Go", command=lambda: GoButtonFunc(x, GoButton), anchor="s")
        GoButton.pack()


def GoButtonFunc(x, GoButton):
    AntwoordList.append(SelectedAntwoord.get())
    print(AntwoordList)
    for i in range(len(Antwoorden[x])):
        RadioList[int(i)].destroy()
    RadioList.clear()
    Vragen[x].destroy()
    GoButton.destroy()
    VraagFunc(x=x + 1)


def AntDisplay():
    AntLabel = Label(root, text="Uw antwoorden:")
    AntLabel.pack()
    for i in range(len(AntwoordList)):
        l = Label(root, text=AntwoordList[i])
        AntwoordLabels.append(l)
        l.pack()


StartButton.configure(command=lambda: VraagFunc())

root.mainloop()
