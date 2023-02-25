class Point:
    def __init__(self, x, y):

        self.x = x
        self.y = y

def vertical(point1, point2):

    return abs(point1.x - point2.x) < 0.00001

def computeSlope(A, B):

    return (B.y - A.y ) / (B.x - A.x)

def parallel( point1, point2, point3, point4 ):

    if vertical(point1, point2) is True:

        if vertical(point3, point4) is True:
           print("Parallel with Axe Oy")
           return True

    return abs(computeSlope(point1, point2) - computeSlope(point3, point4)) < 0.00001

def func():

    point1 = Point(5,7)
    point2 = Point(1,3)
    point3 = Point(7,1)
    point4 = Point(9,3)

    if parallel(point1, point2, point3, point4) is True:

        print("The lines are parallels.")

    else:
        print("The lines are not parallels.")
func()
