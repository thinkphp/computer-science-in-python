def main():
	# solved iteratively
	n = 10
	line = 1
	space = n - 1
	c = 1
	while line <= n:
		for i in range(1,space+1):
			print(" ", end = "")
		for i in range(1, c + 1):
		    print("*", end = "")	
		print("")    
		line = line + 1
		space = space - 1
		c += 2
main()	
