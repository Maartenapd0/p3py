from tkinter import *
window = Tk()

label = Label(
    text="Hello, Tkinter",
    fg="white",
    bg="blue",
)
entry = Entry()

entry.pack()
label.pack()
window = mainloop()