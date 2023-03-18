def func():
    def subset(working_set, k, n):
    	if k == n:
    	   s = {k for k in working_set if working_set[k] == 1}
    	   solutions.append(s)
    	else:
    		k+=1
    		for i in [0,1]:
    			working_set[k] = i
    			print(working_set)
    			subset(working_set, k, n)
    global solutions
    solutions = []
    n = 3
    subset({}, 0, n)
    print(solutions)
func()    	
