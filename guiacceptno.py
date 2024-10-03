from tkinter import END, Button, Entry, Label, Tk


def printWord(N):
    i = 0
    length = len(N)
    while i < length:     
        printValue(N[i])
        i += 1
        
def printValue(digit):
    if digit == '0':
        wordField.insert(30,'ZERO ')
    elif digit == '1':
        wordField.insert(30,'ONE ')
    elif digit == '2':
        wordField.insert(30,'TWO ')
    elif digit=='3':
        wordField.insert(30,'THREE ')
    elif digit == '4':
        wordField.insert(30,'FOUR ')
    elif digit == '5':
        wordField.insert(30,'FIVE ')
    elif digit == '6':
        wordField.insert(30,'SIX ')
    elif digit == '7':
        wordField.insert(30,'SEVEN ')
    elif digit == '8':
        wordField.insert(30,'EIGHT ')
    elif digit == '9':
        wordField.insert(30,'NINE ')
        
def clearAll() :
    numberField.delete(0, END)
    wordField.delete(0, END)
    

def wordconvert():
    
    number0 = numberField.get()
    printWord(number0)

if __name__=="__main__" :
    gui = Tk()
    gui.configure(background = "light green")
    gui.title("decimal number converter")
    gui.geometry("300x125")
    number = Label(gui, text = "Give number", bg = "#00ffff")
    number1 = Label(gui, text = "number", bg = "light green")
    numberField = Entry(gui)
    result = Label(gui, text = "result", bg = "#00ffff")
    resultbutton = Button(gui, text = "Result button",fg = "Black",
    bg = "gray", command = wordconvert)
    numberinword = Label(gui, text ="number in word",bg ="light green")
    wordField = Entry(gui)
    clearAllEntry = Button(gui, text = "Clear All", fg ="Black",
    bg = "gray", command = clearAll)
    
    number.grid(row = 0, column = 1)
    number1.grid(row = 1, column = 1)
    numberField.grid(row = 2, column = 1)
    resultbutton.grid(row = 3, column = 1)
    
    result.grid(row = 0, column = 5)
    numberinword.grid(row = 1, column = 5)
    wordField.grid(row = 2, column = 5)
    clearAllEntry.grid(row = 3, column = 5)
    gui.mainloop()
