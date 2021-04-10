from tkinter import *
import random
window = Tk()

window.geometry ("300x300")

andwoord = Label(window, text="")


def show(event):
    getal = random.randint(0, 6)
    ruimte = Label(window, text=getal)
    andwoord.configure(text=getal)


label = Label()
btn_submit = Button(master=label, text="dobbel", command = show) 
btn_submit.place(x=25, y=100)
btn_submit.pack()



def dobbelen(event):
    print(getal)

btn_submit.bind("<Button-1>", show)


window = mainloop()