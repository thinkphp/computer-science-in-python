def fn():
    def abs(a,b):
        if a > b:
            return a - b
        else:
             return b - a
    def init():
        stack[level] = 0
    def succ():
        if stack[level]<n:
            stack[level]+=1
            return 1
        return 0
    def valid():
        for i in range(1, level):
            if stack[i] == stack[level] or abs(stack[i],stack[level]) == abs(i,level):
                return 0
        return 1

    def sol():
        return level == n

    def printf():
        for i in range(1, n+1):
            print(stack[i], i, end = " ")
            print()
    def solve():
        global level
        level = 1
        init()
        while level > 0:
            a = 1
            b = 0
            while a and not b:
                a = succ()
                if a:
                    b = valid()
            if a:
                if sol():
                    printf()
                    break
                else:
                    level+=1
                    init()
            else:
                level-=1

    n = int(input())
    stack = [0] * (n+1)
    solve()
    matrix = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        matrix[stack[i]][i] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if matrix[i][j] == 1:
                print("*", end =" ")
            else:
                print("_", end = " ")
        print()
fn()
