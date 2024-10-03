from tkinter import *

top = Tk()
top.title('Course')
top.geometry("300x250")
Lb1 = Listbox(top,fg='yellow',width=30,bg='gray',bd=1,activestyle='dotbox')
label=Label(top,text='Computer Science Course Listing').pack()
Lb1.insert(1, "Computer Programming")
Lb1.insert(2, "Information Science")
Lb1.insert(3, "Networking")
Lb1.insert(4, "Operating Systems")
Lb1.insert(5, "Artificial Intelligence")
Lb1.insert(6, "Information Technology")
Lb1.insert(7,'Information Security')
Lb1.insert(8, "Cyber Security")

Lb1.pack()
top.mainloop()
