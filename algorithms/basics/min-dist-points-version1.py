def sqrt(n):
    x = n
    y = 1.0
    eps = 0.0000001
    while x - y > eps:
        x = (x + y) / 2
        y = n / x
    return x
def computeDistance(x0,y0,x,y):
    return sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
def main():
 
    print("Point#0:")
    x0 = float(input("abs="))
    y0 = float(input("ord="))
 
    n = int(input("number of points N = "))
 
    print("Point#1:\n")
    x1 = float(input("abs="))
    y1 = float(input("ord="))
    dist = computeDistance(x0,y0,x1,y1)
 
    for i in range(2,n+1):
      print("Point#%d:"%i)
      x = float(input("abs="))
      y = float(input("ord="))
      d = computeDistance(x0,y0,x,y)
      if d < dist:
          x1 = x
          y1 = y
          dist = d
 
    print("The minimum distance = %.5f and the closest point is (%.2f,%.2f)"%(dist,x1,y1))
 
main()
