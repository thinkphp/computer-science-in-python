from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry('300x300')

equation = ''

def buttonClicked(button):
    global equation
    global entry
    equation.join(button)

    if button == "=":
        entry.delete(0,20)
        entry.insert(0,eval(equation))
        equation = str(eval(equation))
    elif button == "c":
        entry.delete(0,20)
        equation = ''
    else:
        equation = equation+button
        entry.delete(0,20)
        entry.insert(0,equation)

entry = Entry(window, bd = 4, width = 30, font =('Courier New', 10,'bold'), justify = 'right')
entry.place(x=30,y=10)

one = Button(text = '1', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('1'))
one.place(x=55,y=50)
two = Button(text = '2', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('2'))
two.place(x=105,y=50)
three = Button(text = '3', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('3'))
three.place(x=155,y=50)
multiply = Button(text = '*', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('*'))
multiply.place(x=205,y=50)
four = Button(text = '4', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('4'))
four.place(x=55,y=94)
five = Button(text = '5', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('5'))
five.place(x=105,y=94)
six = Button(text = '6', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('6'))
six.place(x=155,y=94)
divide = Button(text = '/', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('/'))
divide.place(x=205,y=94)
seven = Button(text = '7', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('7'))
seven.place(x=55,y=138)
eight = Button(text = '8', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('8'))
eight.place(x=105,y=138)
nine = Button(text = '9', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('9'))
nine.place(x=155,y=138)
minus = Button(text = '-', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('-'))
minus.place(x=205,y=138)
minus = Button(text = '-', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('-'))
minus.place(x=205,y=138)
clear = Button(text = 'C', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('c'))
clear.place(x=55,y=182)
zero = Button(text = '0', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('0'))
zero.place(x=105,y=182)
decimal = Button(text = '.', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('.'))
decimal.place(x=155,y=182)
plus = Button(text = '+', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('+'))
plus.place(x=205,y=182)
equal = Button(text = '=', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = lambda:buttonClicked('='))
equal.place(x=205,y=226)
exit = Button(text = 'Exit', justify = 'center', width = 5, height = 2, font = ('Courier New', 10,'bold'), command = window.destroy)
exit.place(x=55,y=226)

mainloop()
