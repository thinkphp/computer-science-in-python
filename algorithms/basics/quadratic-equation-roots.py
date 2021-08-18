import math

def readCoefficient():

    #first coefficient
    a = float(input("a = "))

    #second coefficient
    b = float(input("b = "))

    #third coefficient
    c = float(input("c = "))

    #return the coefficients a, b, c
    return a,b,c

def main():
    a,b,c = readCoefficient()
    delta = b * b - 4 * a * c
    S = -b / a
    P = c / a

    if delta > 0:
       if S > 0:
          if P > 0:
             print("x1 > 0, x2 > 0")
          elif P < 0:
             print("x1 < 0, x2 > 0, |x1| > |x2| ")
          else:
             print("x1 > 0, x2 = 0")
       elif S < 0:
          if P > 0:
             print("x1 < 0, x2 < 0")
          elif P < 0:
             print("x1 > 0, x2 < 0 , |x1| < |x2| ")
          else:
             print("x1 > 0, x2 = 0")

    elif delta < 0:
        print("Solutions are in Complex Numbers!")

    print("\nVerification:\n")
    if delta > 0:
        x1 = (-b+math.sqrt(delta)) / 2 * a
        x2 = (-b-math.sqrt(delta)) / 2 * a
        print(f"x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x1 = x2 = -b/2*a
        print(f"x1 = x2 = {x1}")
    else:
        realPart = -b/2*a
        imaginaryPart = math.sqrt(-delta)/2*a
        print(f"x1 = {realPart} + {imaginaryPart} i,\nx2 = {realPart} - {imaginaryPart} i")
main()
