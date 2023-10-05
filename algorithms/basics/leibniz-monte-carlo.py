import math
import random

def monte_carlo2():

    circle_points = 0

    square_points = 0

    interval = 1000

    for i in range(interval**2):

        x = random.uniform(-1,1)

        y = random.uniform(-1,1)

        dist = x**2+ y**2

        if dist <= 1:

            circle_points+=1

        square_points+=1

        pi = 4 * circle_points / square_points

    print("Approximation of PI ~", pi)

def monte_carlo(repeats = 10**5):

    count = 0

    for _ in range(0,repeats+1):

        x, y = random.random(), random.random()

        if x*x + y*y <= 1:

            count+=1

    return (float) (4*count)/repeats


#
# Leibniz's Serie Taylor
# pi ~ 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 ...)
#

def leibniz(terms):

    sum = 0

    for i in range(terms+1):

        term = (-1) ** i / (2*i+1)

        sum += term

    return 4*sum

#
# 1 - 1/3 + 1/5 - 1/7 + 1/9 -...
#
def leibniz2():

    sign = 1

    t1 = 1

    t2 = 1 - 1/3

    i = 5

    eps = 0.00001

    while 4 * (t1 - t2 if t1 > t2 else t2 - t1) >= eps:

          t1 = t2

          t2 += sign * float(1/i)

          sign *= -1

          i+=2

    return 4 * t2

def main():

    terms = int(input("Enter the number of terms Terms = "))

    PI = leibniz(terms)

    print("PI (Leibniz Method) ~ %f"%PI)

    _PI = monte_carlo()

    __PI = leibniz2()

    print("PI (Monte Carlo Method) ~ %f"%_PI)

    print("PI (Leibniz method) ~ %f"%__PI)

    print("PI (function built-in Python) ~ %f"%math.pi)

    #monte_carlo2()

main()
