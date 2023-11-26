# Square
def sqr( n ):
    return n * n

#Square Root
def sqrt( n ):

    x = n
    y = 1.0
    eps = 0.000001

    while x - y > eps:
        x = (x + y) / 2
        y = n / x
    return x

# ax + b = 0
def FirstDegreeEquation(a, b):

    if a == 0:

        if b == 0:

            print("Ecuatia are o infinitate de solutii!")

        else:

            print("Ecuatia nu are solutii")
    else:

        if b == 0:

            print("x = 0")

        else:

            print("x = ", -b/a)

# ax^2 + bx + c = 0
def QuadraticEquation(a, b, c):

    if a != 0:
    
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0 and a > 0:
            root1 = (-b - sqrt(discriminant))/(2*a)
            root2 = (-b + sqrt(discriminant))/(2*a)
            return 2, root1, root2
        elif discriminant > 0 and a < 0:
            root1 = (-b + sqrt(discriminant))/(2*a)
            root2 = (-b - sqrt(discriminant))/(2*a)
            return 2, root1, root2
        elif discriminant == 0:
            root1 = root2 = -b/(2*a)
            return 1, root1
        else:
            return [0]
    else:
        if b == 0 and c == 0:
            return [-1]
        elif b != 0:
            root1 = -c/b
            return [1, root1]
        else:
            return[0]
