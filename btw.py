from tkinter import *
#window maken
window = Tk()
#Variable
variable = StringVar(window)
#window title
window.title("btw calculator")
#format
window.geometry("300x300")
#labels
bedrag = Label(window, text="bedrag")
hooglaag = Label(window, text="selecteer hoog of laag btw")
antwoord = Label(window, text="")
#inputs
bedragInvoer = Entry(window,width=5)
hoogLaaginvoer = OptionMenu(window, variable, "hoog btw", "laag btw")
#grid
bedrag.grid(column=0,row=0)
bedragInvoer.grid(column=1,row=0)

hooglaag.grid(column=0,row=1)
hoogLaaginvoer.grid(column=1,row=1)

antwoord.grid(column=0,row=2)
#functie
def Clear():
    bedragInvoer.delete(0, "end")
def btw():
    if variable.get() == "hoog btw":
        bedrag = float(bedragInvoer.get()/100*121)
        return bedrag
    elif variable.get() == "laag btw":
        bedrag = float(bedragInvoer.get()/100*109)
        return bedrag
    else:
        bedrag = "voer hoog of laag btw in"
        return bedrag
    antwoord.configure(text= bedrag)


#buttons
button1 = Button(window, text="bereken", command=btw)
button1.grid(column=1, row=3)

button2 = Button(window, text="wis", command= Clear)
button2.grid(column=1, row=5)
#main-loop
window.mainloop()