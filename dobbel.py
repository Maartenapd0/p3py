from tkinter import *
import random
window = Tk()

window.geometry ("300x300")

andwoord = Label(window, text="")
andwoord.grid(column = 1, row = 2)


def show():
    getal = random.randint(0, 6)
    ruimte = Label(window, text=getal)
    andwoord.configure(text=getal)


label = Label()
btn_submit = Button(master=window, text="dobbel", command = show) 
btn_submit.grid(column = 1, row = 1)


def dobbelen(event):
    print(getal)




window.mainloop()