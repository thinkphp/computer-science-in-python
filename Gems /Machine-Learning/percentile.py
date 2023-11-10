import numpy
import math

#Percentile for Machine Learning
# Mean, median, mode

#un array de varste
#populatia unui sat
ages = [ 5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82,32,2, 8, 6, 25, 36, 27, 61, 31 ]

print(ages)

percentila = 75
#size-ul vectorului
n = len(ages)

print("size=", n)

ages.sort()

x = numpy.percentile(ages, 75)

index = math.ceil(75/100*n)

print("75% din populatia satului sunt de ",ages[ index - 1 ], " de ani sau mai tineri")

print("math.ceil",math.ceil(17.2))
print(x)
