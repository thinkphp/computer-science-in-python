class Complex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag
    def module(self):
        return sqrt(self.real*self.real + self.imag*self.imag)
    def add(self,ob):
        return Complex(self.real + ob.real, self.imag + ob.imag)
    def sub(self,ob):
        return Complex(self.real - ob.real, self.imag - ob.imag)
    def __add__(self,ob):
        return Complex(self.real + ob.real, self.imag + ob.imag)
    def __sub__(self,ob):
        return Complex(self.real - ob.real, self.imag - ob.imag)
    def __repr__(self):
        num = str(self.real)
        if self.imag >= 0:
            num += "+"
        num += str(self.imag) + "i"
        return num
def main():
    z1 = Complex(2, 3)
    z2 = Complex(5, 6)
    print(z1)
    print(z2)
    z3 = z1 + z2
    print(z3)
    z = Complex(1)
    z4 = Complex(7,8)
    z5 = z4 + Complex(2)
    print(z5)
main()
