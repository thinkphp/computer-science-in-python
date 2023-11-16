#!/usr/bin/python3
import math

N = int(input().strip())
data = [int(i) for i in input().strip().split(" ")]

d_mean = sum(data) / N

sq_mean = [(i - d_mean)**2 for i in data]

variance = sum(sq_mean) / N

std_dev = math.sqrt(variance)
print("{:.1f}".format(std_dev))
