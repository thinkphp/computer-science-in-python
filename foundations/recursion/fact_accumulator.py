#
# Recursive Factorial with accumulator
#
def fact(n, acc=1):
	
	if n == 0:
		print(n,end=" ")
		return acc
		
	else:
		print(n,end=" ")
		return fact(n-1, acc * n)

print(fact(5))		
