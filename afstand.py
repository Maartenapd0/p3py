import tkinter as tk

#beeld
window = tk.Tk()
window.title('Bereken hoe lang u onderweg bent')

#vraag afstand
label_out = tk.Label(window, text='Wat is de afstand?(in km)')
label_out.pack()
    # antwoord afstand
label = tk.Label(window, text='Afstand:')
label.pack()
    #invul beeld
entry = tk.Entry(master=window, width=10)
entry.pack()

#vraag snelheid
label_out = tk.Label(window, text='Wat is de snelheid?(in uur)')
label_out.pack()
    # antwoord snelheid
label = tk.Label(window, text='Snelheid:')
label.pack()
    #invul beeld
entry = tk.Entry(master=window, width=10)
entry.pack()

#submit knop
btn_sumbit = tk.Button(master=window, text='Submit')
btn_sumbit.pack()

#applicatie starten
window.mainloop()