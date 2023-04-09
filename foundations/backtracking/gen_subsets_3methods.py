def func2():

	def solution(level):
		for i in range(1, level+1):
			print(stack[i], end="")
		print()	

	def solve(level):
		if level <= n:
			for i in range(stack[level-1]+1,n+1):				
				   stack[level] = i				  
				   solution(level)
				   solve(level+1)

	n = 3
	stack = [0] * (n+1)
	solve(1)

func2()	

def func():
    def solve(working_set, level, n):
        if level == n:
        	s = {k for k in working_set if working_set[k] == 1}
        	solutions.append(s)
        else:
            level+=1
            for i in [0,1]:
                working_set[level] = i
                solve(working_set, level, n)	
    n = 3
    solutions = []
    solve({}, 0, n)
    print(solutions)
func()

def func3():

	def init():
		stack[level] = -1

	def succ():
	    if stack[level] < 1:
	       stack[level]+=1
	       return True
	    else:
	       return False

	def valid():
	    return True       

	def sol():
	    return level == n

	def printf():
	    for i in range(1, n+1):
	    	if stack[i] == 1:
	    		print(i, end =" ")
	    print()		


	def solve():
		global level
		level = 1
		init()
		while level > 0:
			h = True
			v = False
			while h and not v:
				h = succ()
				if h:
					v = valid()
			if h:
			   if sol():
			      printf()
			   else:
			      level+=1
			      init()
			else:
			   level-=1         		

	n = 3
	stack = [0] * (n+1)
	solve()
func3()	
