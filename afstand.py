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

#event handler
def handle_submit(event):
    print('knop ingedrukt')
    print(entry.get())
    try:
        tijd = float(entry1.get) / float(entry.get())
        print(tijd)
        label_out['text'] = 'Je doet er ' + str(tijd) + ' uur over.'
    except:
        label_out['text'] = 'Vul alle gegevens in'

btn_sumbit.bind('<Button-1>', handle_submit)
#applicatie starten haalll
window.mainloop()