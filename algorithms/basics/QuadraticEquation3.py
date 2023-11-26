from math import sqrt
 
 
def equation(a, b, c):
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d > 0 and a > 0:
            x1 = (-b - sqrt(d)) / (2 * a)
            x2 = (-b + sqrt(d)) / (2 * a)
            return 2, x1, x2
        elif d > 0 and a < 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            return 2, x1, x2
        elif d == 0:
            x = -b / (2 * a)
            return 1, x
        else:
            return [0]
    else:
        if b == c == 0:
            return [-1]
        elif b != 0:
            x = - c / b
            return 1, x
        else:
            return [0]
 
 
A, B, C = [int(i) for i in input().split()]
print(*equation(A, B, C), sep='\n')
