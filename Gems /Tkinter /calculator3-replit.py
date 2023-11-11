import sys
from tkinter import *


class Calculator(Frame):
    def __init__(self, root):
        super(Calculator, self).__init__(root)
        self.formula = '0'
        self.label = Label(text=self.formula, font=('Calibri', 11, 'bold'),
                           bg='#000', foreground='#FFF')
        self.build()

    def build(self):
        self.label.place(x=5, y=25)

        btns = [
            'C', 'DEL', '*', '=',
            '1', '2', '3', '/',
            '4', '5', '6', '+',
            '7', '8', '9', '-',
            '(', '0', ')', '.'
        ]

        x = 5
        y = 70

        for bt in btns:
            com = lambda x=bt: self.calculate(x)
            Button(text=bt, bg='#FFF',
                   font=('Calibri', 8),
                   command=com).place(x=x,
                                      y=y,
                                      width=57,
                                      height=40)
            x += 58
            if x > 200:
                x = 5
                y += 40

    def calculate(self, operation):
        if operation == 'C':
            self.formula = ''
        elif operation == 'DEL':
            self.formula = self.formula[0:-1]
        elif operation == '=':
            self.formula = str(eval(self.formula))
        # ===== BUGS ========
        elif operation == '.':
            sys.exit()
        elif operation == '+':
            self.formula += '-'
        # ===== BUGS ========
        else:
            if self.formula == '0':
                self.formula = ''
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == '':
            self.formula = '0'
        self.label.configure(text=self.formula)


def start_application():
    root = Tk()
    root['bg'] = '#000'
    root.geometry('242x275+100+100')
    root.title('Calculator')
    root.resizable(False, False)
    app = Calculator(root)
    app.pack()
    return app


if __name__ == '__main__':
    start_application().mainloop()
