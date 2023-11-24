def FirstDegreeEquation(a, b):

    if a == 0:
       if a == b:
          print("The Equation has an infinity solutions.")
       else:
          print("The Equation has not solutions.")
    else:
       if b == 0:
          print("x = 0")
       else:
          print("x = ", -b/a)



def euclid_rec(a,b):

    if b == 0:
        return a
    else:
        return euclid_rec(b, a % b)

def euclid_iter(a,b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def controlDigit(n):
    
    if n % 9 != 0:
        return n % 9
    else:
        return 9;
