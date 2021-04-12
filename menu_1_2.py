from tkinter import *

window = Tk()

window.title("home menu")

window.geometry("300x300")

def afstand():
    import afstand
def btw():
    import btw

def cirkel():
    import Cirkel
def dobbel():
    import dobbel

def raad():
    import getallen_raden

afstand = Button(window, text="afstand", command=afstand)
btw = Button(window, text="btw", command=btw)
cirkel = Button(window, text="cirkel", command=cirkel)
dobbel = Button(window, text="dobbel", command=dobbel)
raad = Button(window, text="raad het getal", command=raad)

afstand.grid(column=1, row=0)
btw.grid(column=1, row=1)
cirkel.grid(column=1, row=2)
dobbel.grid(column=1, row=3)
raad.grid(column=1, row=4)

window.mainloop()