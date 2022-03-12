# solved recursively
def triangle(line, s, c):    
    if line <= n:
    	for i in range(1, s + 1):
    		print(" ", end ="")
    	for j in range(1, c + 1):
    	    print("*", end = "")
    	print("")     
    	triangle(line + 1, s - 1, c + 2)

def main():

	global n
	n = 10
	triangle(1, n - 1, 1) 

main()    
