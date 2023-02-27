
# General Equation Line: ax + by + c = 0
#
# y - y1 = m (x - x1) where m = (y2-y1)/(x2-x1)
#
# y = m x + c where c can be compute replacing a point A(x1,y1) -> c = mx1-y1
#
# a = y1 - y2
# b = x2 - x1
# c = x2y1 - x1y2
#
# ax + by + c = 0
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

    A = Point(5,7,"A")
    B = Point(1,3,"B")

    #Find the equation of the line that passes through the point (x, y) and has a slope
    slope = computeSlope(A.x, A.y, B.x, B.y)


    print(A)
    print(B)
    print("Gradiend = ", slope)

    c = A.y - slope * A.x
    
    print("First method (y = mx + c):")
    print("y = %.2f * x + %.2f"%(slope, c))
    
    print("Second method:")
    print("(y - y1 = m (x - x1)) => y - %.2f = %.2f x - %.2f * %.2f " % (A.y, slope, slope, A.x))

    print("y = %.2f x - %.2f * %.2f + %.2f " % (slope, slope, A.x, A.y))

    print("y = %.2f x + %f " % (slope, -slope * A.x + A.y))
    a = A.y - B.y
    b = B.x - A.x
    c = (A.x * B.y) - (B.x * A.y)
    
    print("Third method (finding the coeffs: a, b, c):")    
    print("Equation Line(ax+by+c=0) => %.2f x+ %.2f y+ %.2f=0"%(a,b,c))
func()
