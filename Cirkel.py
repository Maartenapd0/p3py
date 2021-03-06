import tkinter as tk

#window
window = tk.Tk()
window.title = ("Cirkel berekenen")
window.geometry("300x300")

#vraag 
label_main = tk.Label(window, text="wat is de diameter van de cirkel? in cm! (. geen ,)") 
label_cirkel = tk.Label(text="Diameter: ")
entry_cirkel = tk.Entry(master=window)

#placement van text en text vakken
label_main.grid(row=1, column=0, sticky="w")
label_cirkel.grid(row=2, column=0, sticky="w")
entry_cirkel.grid(row=2, column=0, sticky="e")
label_oppervlakte = tk.Label(text="Oppervlakte: ")
label_oppervlakte.grid(row=4, column=0, sticky="w")
label_omtrek = tk.Label(text="Omtrek: ")
label_omtrek.grid(row=5, column=0, sticky="w")

#text vak voor fout meldingen
label_fout = tk.Label(text="...")
label_fout.grid(row=7, column=0, sticky="w")

#submit button
btn_submit = tk.Button(master=window, text="Submit")
btn_submit.grid(row=6, column=0, sticky="w")

#clear button
btn_clear = tk.Button(master=window, text="Clear")
btn_clear.grid(row=6, column=0)

#main function voor de berekening
def handle_submit(event):
    try:
        pie = 3.14
        diameter = (float(entry_cirkel.get()))
        straal = diameter / 2
        oppervlakte = straal * straal * pie
        omtrek = diameter * pie
        label_oppervlakte["text"] = "Oppervlakte: " + ("%.2f" % oppervlakte) + " cm2"
        label_omtrek["text"] = "Omtrek: " + ("%.2f" % omtrek) + " cm"
    except:
        entry_cirkel.delete(0, "end")
        label_fout["text"] = "Vul een geldige getal in!"

#function voor de clear
def handle_clear(event):
    entry_cirkel.delete(0, "end")
    label_fout["text"] = "..."

#buttons
btn_submit.bind("<Button-1>", handle_submit)
btn_clear.bind("<Button-1>", handle_clear)

#starten
window.mainloop()
#Jarno van Beek
