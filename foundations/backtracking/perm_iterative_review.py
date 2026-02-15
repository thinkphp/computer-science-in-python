def sol():
	return k == n
def init():
    stack[k] = 0

def succ():
	if stack[k]<n:
		stack[k]+=1
		return 1
	return 0
		
def valid():
    for i in range(1, k):
        if stack[i] == stack[k]:
           return 0
    return 1

def display_solution():
    for i in range(1, n+1):
        print(stack[i], end = " ")
    print()               		

def backtracking():
	global k
	k = 1
	init()

	while k > 0:
		s = 1
		v = 0
		while s == 1 and v == 0:
			s = succ()
			if s:
				v = valid()
		if s: 
		   if sol():
		      display_solution()
		   else:
		      k+=1
		      init()
		else:
		   k-=1         		

def main():
	global stack
	global n	
	n = int(input("n="))
	stack = [0] * (n+1)
	#print(stack)
	backtracking()

if __name__ == '__main__':
	main()
