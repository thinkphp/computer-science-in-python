def numberFour(n):
	
	if n - 4 != 0:
		
		if n % 10 == 0:
			
			numberFour( n // 10 )
			
		elif n % 10 == 4:
			
			numberFour( n // 10 )
			
		else:
			numberFour( n * 2 )
			
		print("--->%d"%n, end="")		
	
print("4", end="")

numberFour(1234)		
			
