def fn_it(m):
    def init():
        stack[level] = 0

    def succ():
        global sum
        if stack[level] + sum < n:
            stack[level]+=1
            return 1
        else:
            sum -= stack[level-1]
        return 0

    def valid():
        global sum
        if stack[level] + sum <= n:
            sum += stack[level]
            return 1
        return 0

    def sol():
        return sum == n

    def printf():
        global sum
        for i in range(1, level+1):
            print(stack[i], end =" ")
        sum -= stack[level]
        print()

    def solve():
        global level
        level = 1
        init()

        while level > 0:
            s = 1
            v = 0
            while s and not v:
                s = succ()
                if s:
                    v = valid()
            if s:
                if sol():
                    printf()
                else:
                    level+=1
                    init()
            else:
                level-=1
    global sum
    n = m
    stack = [0] * (n+1)
    sum = 0
    solve()
fn_it(4)

print()

def fn_rec():
    def solve(level):
        global sum
        if sum == n:
            for i in range(1, level):
                print(stack[i], end =" ")
            print()
        else:
            stack[level] = 0
            while stack[level] + sum < n:
                stack[level]+=1
                sum += stack[level]
                solve(level+1)
                sum -= stack[level]

    global sum
    m = int(input("m="))
    n = m
    stack = [0] * (n+1)
    sum = 0
    solve(1)
fn_rec()
