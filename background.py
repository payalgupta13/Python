from tkinter import Button, Entry, Label, Tk


def changecolor():
    newvalue = value.get()
    gui.configure(background = newvalue)
    
gui=Tk()
gui.title("color change.")
gui.configure(background = "gray")
gui.geometry("400x300")

color = Label(gui, text = "color", bg = "gray")
value = Entry(gui)
apply = Button(gui, text = "Apply", fg = "Black", bg = "gray", command = changecolor)

color.grid(row=0,column=0)
value.grid(row=0,column=1)
apply.grid(row=0,column=2)

gui.mainloop()
