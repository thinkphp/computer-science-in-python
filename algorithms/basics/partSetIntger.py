import numpy as np
def func2():
    def solve(level):
        if level == n + 1:
           max = np.max(stack)
           for i in range(1, max+1):
               print("{", end = " ")
               for j in range(1, n + 1):
                   if i == stack[j]:
                       print(j, end = ",")
               print("\b}", end =" ")
           print()
        else:
           stack[level] = 0
           while stack[level] < stack[level-1]+1:
                 stack[level]+=1
                 solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)
func2()


def func():
    def solve(level):
        global sum
        if sum == n:
           for i in range(1, level):
               print(stack[i], end = " ")
           print()
        else:
            stack[level] = 0
            for i in range(1, n+1):
                if stack[level]+sum<n:
                  stack[level] = i
                  sum += stack[level]
                  solve(level+1)
                  sum -= stack[level]
    global sum
    n = 3
    stack = [0] * (n+1)
    sum = 0
    solve(1)
