

import random

import tkinter as tk
window = tk.Tk()

window.geometry("300x300")


#Nummer raden
def gokspelletje(args):
    #makkelijk
    def rol_makkelijk():
        mak_ran = random.randint(0,11)
        gok = int(input("Gok hier het nummer!!"))
        if gok == mak_ran:
            print ("gefeliciteerd je hebt goed gegokt!!")
            print ("Het nummer was " , mak_ran)
        else:
            print ("helaas je hebt het fout :(")
            print ("Het nummer was " , mak_ran)
    #medium
    def rol_mid():
        mak_ran = random.randint(0,51)
        gok = int(input("Gok hier het nummer!!"))
        if gok == mak_ran:
            print ("gefeliciteerd je hebt goed gegokt!!")
            print ("Het nummer was " , mak_ran)
        else:
            print ("helaas je hebt het fout :(")
            print ("Het nummer was " , mak_ran)
    #moeilijk
    def rol_moeilijk():
        mak_ran = random.randint(0,111)
        gok = int(input("Gok hier het nummer!!"))
        if gok == mak_ran:
            print ("gefeliciteerd je hebt goed gegokt!!")
            print ("Het nummer was " , mak_ran)
        else:
            print ("helaas je hebt het fout :(")
            print ("Het nummer was " , mak_ran)






    #Moeilijkheid selecteren
    print ("Voor makkelijk (0 t/m 10) voer 1 in!")
    print ("Voor middelmatig (0 t/m 50) voer 2 in!")
    print ("Voor moeilijk (0 t/m 100) voer 3 in!")
    moelijkheid = int(input("Voer hier de gewenste moeilijkheid in"))


    if moelijkheid == 1:
        rol_makkelijk()
    elif moelijkheid == 2 :
        rol_mid()
    else:
        rol_moeilijk()

#button
spelen = tk.Button(master=window,
                   text="spelen",
                   command=lambda: gokspelletje
                   )
spelen.bind("<Button-1>", gokspelletje )

spelen.pack()
#Getallen rader door Rik
