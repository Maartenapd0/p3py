from tkinter import *
import random
window = Tk()

window.geometry ("200x300")

antwoord = Label(window, text="")

def show():
    getal = random.randint(0, 6)
    antwoord.configure(text=getal)

label = Label()
btn_submit = Button(window, text="dobbel", command = show) 
#grid
antwoord.grid(column=0,row=0)
btn_submit.grid(column=0,row=1)


window.mainloop()