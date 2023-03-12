def func():
    def perm(level):
        if level > n:
            for i in range(1, n+1):
                print(stack[i], end=" ")
            print()    
        else:
            for i in range(1, n+1):
              if explored[i] == 0:
                stack[level] = i
                explored[i] = 1
                perm(level+1)
                explored[i] = 0
    n = 3
    stack = [0] * (n+1)
    explored = [0] * (n+1)
    perm(1)
func()
