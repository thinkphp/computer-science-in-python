import numpy
import statistics
import math

speed = [86,87,88,86,87,85,86]

length= int( len(speed) )

mean = sum( speed ) / length

ans = sum((i - mean) ** 2 for i in speed) / length

print("The variance of list is : " + str(math.sqrt(ans)))

print( numpy.std(speed ) )

print( statistics.stdev( speed ) )
