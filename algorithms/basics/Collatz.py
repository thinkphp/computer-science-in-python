
#
# The collatz sequence is a conjecture in mathematics that follows a sequence. This sequence is defined below:
# The sequence begins with any positive integer, say n
# If the integer n is odd, the next number in sequence would be 3n+1
# If the integer n is even, the next number in sequence would be n/2
# The sequence will continue until digit 1 is encountered
#
#

def Collatz(n):
	
	while True:
		
		yield n
		
		if n == 1:
			
			break
		
		if n % 2 != 0:
			
			n = 3 * n + 1
		
		else:
			
			n = n // 2
	
def main():
	
	for i in Collatz(200):
		
		print(i, end = " ")
main()		
