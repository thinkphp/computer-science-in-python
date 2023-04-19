def init():
    stack[level] = 0

def succ():
    global s
    if stack[level] + s < n:
        stack[level] +=1
        return True
    else:
        s -= stack[level-1]
        return False

def sol() -> bool:
    return s == n

def valid():
    global s
    if stack[level] + s <= n:
        s+= stack[level]
        return True
    return False

def printf():
    global s
    for i in range(1, level+1):
        print(stack[i], end =" ")
    print()    
    s-=stack[level]

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

def func():
    global stack, s, n
    n = 4
    stack = [0] * (n + 1)
    s = 0
    solve()
func()
