#
# Filename:
#    partitionNumber.py
#
# Description:
#    Partition of a number
#
def func():
    global s, n
    def init():
        if level == 1:
            stack[level] = 0
        else:
            stack[level] = stack[level-1]-1

    def succ():
        global s
        if stack[level] < (n - s):
            stack[level] += 1
            return True
        else:
            s = s - stack[level-1]
            return False

    def valid():
        global s
        if stack[level] <= n - s:
            s = s + stack[level]
            return True
        return False

    def printf():
        global s
        for i in range(1, level+1):
            print(stack[i], end = " ")
        s -= stack[level]
        print()

    def sol():
        return s == n

    def backtracking():
        global level, s
        s = 0
        level = 1
        init()
        while level > 0:
            h = True
            v = False
            while h is True and v is False:
                h = succ()
                if h is True:
                    v = valid()
            if h is True:
                if sol() is True:
                    printf()
                else:
                    level+=1
                    init()
            else:
                level-=1

    n = 4
    stack = [0] * (n+1)
    backtracking()

func()
