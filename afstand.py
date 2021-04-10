import tkinter as tk

#beeld
window = tk.Tk()
window.title('Bereken hoe lang u onderweg bent')
window.geometry("300x300")

#vraag afstand
label_out1 = tk.Label(window, text='Wat is de afstand?(in km)')
    # antwoord afstand
label1 = tk.Label(window, text='Afstand:')
    #invul beeld
entry1 = tk.Entry(master=window, width=10)
        
#vraag snelheid
label_out = tk.Label(window, text='Wat is de snelheid?(in uur)')  
    # antwoord snelheid
label = tk.Label(window, text='Snelheid:')
    #invul beeld
entry = tk.Entry(master=window, width=10)
        
#submit knop
btn_sumbit = tk.Button(master=window, text='Submit')
        
# grid
label_out1.grid(row=1, column=0, sticky="w")
label1.grid(row=2, column=0, sticky="w")
entry1.grid(row=2, column=1, sticky="e")
label_out.grid(row=4, column=0, sticky="w")
label.grid(row=5, column=0, sticky="w")
entry.grid(row=5, column=1, sticky="e")
btn_sumbit.grid(row=7, column=1, sticky='w')

#event handler
def handle_submit(event):
    print('knop ingedrukt')
    try:
        afstand = float(entry1.get()) / float(entry.get())
        print(afstand)
        label_out['text'] = 'Je doet er ' + str(afstand) + ' uur over.'
    except:
         label_out['text'] = 'Vul gegevens in.'

btn_sumbit.bind('<Button-1>', handle_submit)

#applicatie starten 
window.mainloop()

# Floor Deuss
