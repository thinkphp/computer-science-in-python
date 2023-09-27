def sqrt(n):
    x = n
    y = 1.0
    e = 0.000001
    while x - y > e:
        x = (x + y) / 2
        y = n / x
    return x

class Point:
    def __init__(self,x,y,index=0):
        self.x = float(x)
        self.y = float(y)
        self.index = int(index)

    def setIndex(self, index):
        self.index = int(index)
    def __repr__(self):
        return "Point(" + str(self.x) + "," + str(self.y) + ")"

def computeDist(p,q):
    return sqrt((q.x - p.x)*(q.x - p.x) + (q.y - p.y)*(q.y - p.y))

def readPoint(p):
  p.x = float(input("abs="))
  p.y = float(input("ord="))

def main():
    print("Point#0")
    p0 = Point(0,0,0)
    readPoint(p0)
    print(p0)

    n = int(input("Number of point: N="))

    print("Point#1")
    p1 = Point(0,0,1)
    readPoint(p1)
    print(p1)

    dist = computeDist(p0,p1);

    print(dist)

    for i in range( 2, n + 1 ):

        p = Point(0,0,i)
        p.setIndex(i)
        print("Point#%d"%i)
        readPoint(p)
        print(p)
        d = computeDist(p0, p)
        print(d)
        if d < dist:
           dist = d
           print("Found Point:")
           p1 = p
           print(p1)

    print("\nMinimum Distance = %f\nThe closest point = P#%d(%.2f, %.2f)"%(dist, p1.index, p1.x, p1.y))
main()
