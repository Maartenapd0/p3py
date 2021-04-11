from tkinter import *
from tkinter import filedialog
import os

#beeld
window = Tk()
window.title('start menu')
window.geometry("200x300")

#files



#functies 
def show_test():
    frame_tester.pack_forget()
    frame_test.pack()
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\grkoh\\OneDrive\\Documenten\\GitHub\\p3py", title= "afstand", filetypes=(("py files", "afstand.py"),("all files", "*.*")))
    os.system(filename)


def show_testen():
    frame_tester.pack_forget()
    frame_test.pack()
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\grkoh\\OneDrive\\Documenten\\GitHub\\p3py", title= "btw", filetypes=(("py files", "btw.py"),("all files", "*.*")))
    os.system(filename)

def show_teste():
    frame_tester.pack_forget()
    frame_test.pack()
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\grkoh\\OneDrive\\Documenten\\GitHub\\p3py", title= "Cirkel", filetypes=(("py files", "Cirkel.py"),("all files", "*.*")))
    os.system(filename)

def show_tester():
    frame_tester.pack()
    frame_test.pack_forget()
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\grkoh\\OneDrive\\Documenten\\GitHub\\p3py", title= "dobbelen", filetypes=(("py files", "dobbel.py"),("all files", "*.*")))
    os.system(filename)

def show_testi():
    frame_tester.pack_forget()
    frame_test.pack()
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\grkoh\\OneDrive\\Documenten\\GitHub\\p3py", title= "getallen_raden", filetypes=(("py files", "getallen_raden.py"),("all files", "*.*")))
    os.system(filename)

#menu maken
menubar = Menu(window)
window.config(menu=menubar)


#menu itmes
mainmenu = Menu(menubar)
mainmenu.add_command(label='afstand', command=show_test)
mainmenu.add_command(label='btw', command=show_testen)
mainmenu.add_command(label='cirkel', command=show_teste)
mainmenu.add_command(label='dobbelen', command=show_tester)
mainmenu.add_command(label='getallen_raden', command=show_testi)
mainmenu.add_separator()
mainmenu.add_command(label='sluiten', command=window.quit)
menubar.add_cascade(label='Menu', menu=mainmenu)

# frame voor test 
frame_test = Frame(borderwidth=10)
label_1 = Label(frame_test, text='Iets', bg='white', fg='white', width=20, height=8)
label_1.pack()

# frame voor tester
frame_tester = Frame(borderwidth=10)
label_2 = Label(frame_tester, text='ok', bg='white', fg='white', width=20, height=8)
label_2.pack()


#begin met beeld 1
show_test()
# start aplicatie
window.mainloop()