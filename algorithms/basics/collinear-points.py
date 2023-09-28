class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def checkCollinearity(P1,P2,P3):
    if P1.x*(P2.y-P3.y) - P1.y*(P2.x-P3.x) + P2.x*P3.y - P2.y*P3.x == 0:
       return True
    else:
       return False
def main():
    Points = []
    for i in range(3):
        print("Point#%d"%(i+1))
        x = float(input("abs="))
        y = float(input("ord="))
        P = Point(x,y)
        Points.append(P)
    #method 1 with Slope    
    if Points[0].x == Points[1].x or Points[0].x == Points[2].x:
       if Points[0].x == Points[2].x:
           print("Collinear.")
       else:
           print("No Collinear.")
    else:
        if((Points[1].y - Points[0].y)/(Points[1].x - Points[0].x) == (Points[2].y - Points[1].y)/(Points[2].x - Points[1].x)):
            print("Collinear.")
        else:
            print("No Collinear.")
 
    #method 2 with Sarrus
    if(checkCollinearity(Points[0], Points[1], Points[2]) is True):
            print("Collinear.")
    else:
            print("No Collinear.")
main()
