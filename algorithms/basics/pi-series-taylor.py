import random
import math
#with Series Taylor 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... )
def leibniz2():
    term1 = 1
    term2 = 1 - 1/3
    eps = 0.00001
    sign = 1
    i = 5
    while 4 * (term1 - term2 if term1 > term2 else term2 - term1) >= eps:
          term1 = term2
          term2 += sign * 1 / i
          sign *= -1
          i+=2
    return 4 * term2
def leibniz1(repeats = 1000):
    sum = 0
    for i in range(repeats+1):
        sum += pow(-1,i) / (2 * i + 1)
    return 4 * sum

#
#  pi   number of points generated inside the circle
#  -- = ---------------------------------------------
#  4    number of points generated inside the square
#
def monte_carlo(repeats = 10**5):
    square_count, circle_count = 0, 0
    for i in range(0, repeats):
        x, y = random.random(), random.random()
        if x*x+y*y <= 1:
            circle_count+=1
        square_count+=1
    return 4 * circle_count / square_count

def main():
    print(leibniz2())
    print(leibniz1())
    print(monte_carlo())
    print("PI Built-in Python",math.pi)
main()
