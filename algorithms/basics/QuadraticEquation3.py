#Square Root
def sqrt( n ):
 
    x = n
    y = 1.0
    eps = 0.000001
 
    while x - y > eps:
        x = (x + y) / 2
        y = n / x
    return x
 
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
A, B, C = [int(i) for i in input().split()]
print(*QuadraticEquation(A, B, C), sep='\n')
