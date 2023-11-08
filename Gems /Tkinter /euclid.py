from tkinter import *

# setting up the tkinter window
window = Tk()

window.title("Euclid's algorithm")
window.geometry("600x400")

# creating labels
label1 = Label(window, text = "a = ")
label2 = Label(window, text = "b = ")
result = Label(window, text = "Result = ")

#arranging the widgets
label1.place(x=100, y=50)
label2.place(x=100, y=100)
result.place(x=100, y=150)

# Creating Widgets entry
textfield1 = Entry(window, width=12, font=('Arial 14'), bg="yellow")
textfield2 = Entry(window, width=12, font=('Arial 14'), bg="yellow")
textfield3 = Entry(window, width=10, font=('Arial 14'),bg="lightgreen")

textfield1.place(x=150, y=50)
textfield2.place(x=150, y=100)
textfield3.place(x=180, y=150)

def gcd(a,b):
    while a!=b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def reset():
        textfield1.delete(0, END)
        textfield2.delete(0, END)
        textfield3.delete(0, END)

def euclid():
    num1 = int(textfield1.get())
    num2 = int(textfield2.get())
    result = gcd(num1, num2)
    textfield3.delete(0, END)
    textfield3.insert(END, str(result))

btnRun = Button(window, text='Euclid', height= 5, width=10, command=euclid)
btnRun.place(x=140,y=300)
btnReset = Button(window, text='Reset', height= 5, width=10,  command=reset)
btnReset.place(x=300,y=300)

# window. mainloop() tells Python to run the Tkinter event loop.
# This method listens for events,
# such as button clicks or keypresses, and blocks any code that comes
# after it from running until the window it's called on is closed.
window.mainloop()
