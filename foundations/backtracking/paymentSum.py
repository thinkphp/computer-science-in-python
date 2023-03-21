def func():
    sum = 10
    a = [0,1,2,3,5]
    def printf(level):
        for i in range(1, level):
            print(stack[i], " - ", a[i], end = " ")
        print()

    def solve(level):
        global s
        if s == sum:
            printf(level)
        else:
            stack[level] = -1
            while level < len(a) - 1 and stack[level]*a[level] + s < sum:
                  stack[level] += 1
                  s += stack[level]*a[level]
                  solve(level+1)
                  s -= stack[level]*a[level]
    global s
    s = 0
    stack = [0] * (sum+1)
    solve(1)
func()
