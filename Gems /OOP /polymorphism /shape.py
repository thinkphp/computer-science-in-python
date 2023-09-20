# Polymorphism OOP
class Shape:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def printf(self):
        print("Side = ", self.side)

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return  3.14 * self.radius * self.radius
    def printf(self):
        print("Circle(R = %.2f)"%self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def printf(self):
        print("Rectangle(L = %.2f and W = %.2f)"%(self.length, self.width))

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
    def printf(self):
        print("Triangle(base = %.2f and heigth = %.2f)"%(self.base, self.height))

class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self, side)

def fn():
  c = Circle(5)
  c.printf()
  print("Area = ", c.area())

  r = Rectangle(7,10)
  r.printf()
  print("Area = ", r.area())

  t = Triangle(7,10)
  t.printf()
  print("Area = ", t.area())

  sq = Square(5)
  print("Area Square = ", sq.area())
  sq.printf()
fn()
