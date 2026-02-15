def ok(k):
	for i in range(1, k):
	    if stack[k] == stack[i]:
	       return 0
	return 1        
def perm_rec( k ):
	for i in range(1, n + 1):
		stack[k] = i
		if ok( k ):
			if n == k:
				for i in range(1, n + 1):
					print(stack[i], end = " ")
				print()
			else:
				perm_rec(k + 1)   	  

def perm( k ):	
	if n + 1 == k:
		for i in range(1,n+1):
			print(stack[i], end = ' ')
		print()
	else:
	    for i in range(1, n+1):
	    	if not used[i]:
	    		stack[k] = i
	    		used[i] = 1
	    		perm(k+1)
	    		used[i] = 0
def main():
	global n
	global stack
	global used
	n = int(input("n="))
	stack = [0] * (n + 1)	
	used = [0] * (n + 1)
	perm_rec( 1 )

main()	
