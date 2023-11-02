#Generator infinite: Primes, Fibonacci and Collatz
#Author: Adrian Statescu <mergesortv@gmail.com>
def P():
	n = 2	
	while True:
		j = 2
		prime = 1
		while j * j <= n and prime == 1:
			prime = n % j != 0
			j += 1
		if prime:
		   yield n
		n += 1	
 
def F():
	a, b = 0, 1
	while True:
	      c, a, b = a, b, a + b
	      yield c
 
def Collatz(n):
 
    while True:
    	yield n
    	if n == 1:
    	   break
    	if n & 1:
    	   n = 3 * n + 1
    	else:
    	   n = n // 2    	
 
for i in F():
	print(i, end = ' ')
	if i > 10000:
	   break		   
 
print()
print()
 
for j in Collatz(1780):
    print(j, end = ' ')
print()
print()
 
for k in P():
    print(k, end = ' ')
    if k > 100000:
       break
 
