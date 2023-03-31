def setPartitions():
    def solve(level):
        if level == n+1:
            print(stack)
        else:
            for i in range(1,n+1):
                stack[level] = i
                if stack[level] <= stack[level-1]+1:
                    solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)
setPartitions()

def fulfilled():
    def solve(level):
        global sum
        if sum == n:
           for i in range(1, level):
               print(stack[i], end =" ")
           print()
        else:
           stack[ level ] = 0
           while stack[level]+sum < n:
               stack[level] += 1
               sum += stack[level]
               solve(level+1)
               sum -= stack[level]
    n = 3
    global sum
    stack = [0] * (n+1)
    sum = 0
    solve(1)
fulfilled()
