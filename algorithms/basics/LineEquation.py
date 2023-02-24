#
# General Equation Line: ax + by + c = 0
# y - y1 = m (x - x1) with slope
# y = m x + c
#
class Point():
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
    def __repr__(self):
        return self.name + '(' + str(self.x) + "," + str(self.y) + ')'

def computeSlope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def func():

    A = Point(0,2,"A")
    B = Point(-1,4,"B")

    slope = computeSlope(A.x, A.y, B.x, B.y)

    print(slope)
    print(A)
    print(B)

    c = - slope * A.x + A.y

    print("y = %f * x + %f"%(slope,c))
func()
