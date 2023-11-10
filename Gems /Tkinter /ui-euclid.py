from tkinter import *

#setam o fereastra window
window = Tk()
window.title("App UI Python")
window.geometry("600x450")

#creating labels = etichetele
label1 = Label(window, text = "a = ")
label2 = Label(window, text = "b = ")
#Greatest Common Divisor = cel mai mare divisor comun
result = Label(window, text = "GCD(a,b) = ")

#arrange labels
label1.place(x=100, y=50)
label2.place(x=100, y=100)
result.place(x=100, y=150)

#creating textfields or widgets

textfield1 = Entry(window, width=12, font=('Arial 14'), bg = "yellow")
textfield2 = Entry(window, width=12, font=('Arial 14'), bg = "yellow")
textfield3 = Entry(window, width=12, font=('Arial 14'), bg = "lightgreen")

textfield1.place(x=150, y=50)
textfield2.place(x=150, y=100)
textfield3.place(x=150, y=200)

def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def euclid():
    number_1 = int(textfield1.get())
    number_2 = int(textfield2.get())
    result = gcd(number_1, number_2)
    textfield3.delete(0, END)
    textfield3.insert(0, str(result))

def reset():
    textfield1.delete(0, END)
    textfield2.delete(0, END)
    textfield3.delete(0, END)

btnRun = Button(window, text = "Euclid", height=5, width = 10, command = euclid)
btnReset = Button(window, text = "RESET", height=5, width = 10, command = reset)

btnRun.place(x=140, y=300)
btnReset.place(x=300, y=300)

window.mainloop()
