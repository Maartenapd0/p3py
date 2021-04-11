from tkinter import *

#beeld
window = Tk()
window.title('menu beeld')
window.geometry("300x300")

#functies 
def show_test():
    frame_tester.pack_forget()
    frame_test.pack()

def show_tester():
    frame_tester.pack()
    frame_test.pack_forget()

#menu maken
menubar = Menu(window)
window.config(menu=menubar)

#menu itmes
mainmenu = Menu(menubar)
mainmenu.add_command(label='Test', command=show_test)
mainmenu.add_command(label='Tester ', command=show_tester)
mainmenu.add_separator()
mainmenu.add_command(label='Weg', command=window.quit)
menubar.add_cascade(label='Menu', menu=mainmenu)

# frame voor test 
frame_test = Frame(borderwidth=10)
label_1 = Label(frame_test, text='Iets', bg='purple', fg='white', width=20, height=8)
label_1.pack()

# frame voor tester
frame_tester = Frame(borderwidth=10)
label_2 = Label(frame_tester, text='Iets anders', bg='black', fg='white', width=20, height=8)
label_2.pack()


#begin met beeld 1
show_test()
# start aplicatie
window.mainloop()