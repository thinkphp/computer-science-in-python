#clasa de baza
class Shape:
     def __init__(self, side):
         self.side = side
     def area(self):
         return 0
     def printf(self):
         return 0

#clase derivate:
# -Rectangle, Circle, Triangle

class Rectangle( Shape ):
    def __init__(self, heigth, width):
        self.heigth = heigth
        self.width = width
    def printf(self):
        print("Rectangle: height = %f & width = %f"%(self.heigth, self.width))
    def area(self):
        return self.heigth * self.width


class Circle( Shape ):
    def __init__(self, radius):
        self.radius = radius
    def printf(self):
        print("Circle radius = %f"%(self.radius))
    def area(self):
        return self.radius * 3.14 * self.radius

class Triangle( Shape ):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def printf(self):
        print("Triangle:  base = %f and height = %f"%(self.base, self.height))
    def area(self):
        return self.base * self.height / 2
        #print("%d %d %d"%(a,b,c))
        #       a   b  c
def main():

    c = Circle(5)
    c.printf()
    print("ARiA=", c.area());
    r = Rectangle(10,30)
    r.printf()
    print("ARiA=", r.area());
    t = Triangle(20,90)
    t.printf()
    print("ARiA=", t.area());
main()
