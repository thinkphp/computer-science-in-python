def partition():
    global n, sum, stack
    sum = 0
    n = int(input("n="))
    stack = [0]*(n+1)

    def init(level):
        if level == 1:
            stack[level] = 0
        else:
            stack[level] = stack[level-1] - 1
    def succ(level) -> bool:

        global sum
        if stack[level] < n - sum:
            stack[level] +=1
            return True
        else:
            sum -= stack[level-1]
            return False

    def valid(level) -> bool:
        global sum
        if stack[level] <= n - sum:
            sum += stack[level]
            return True
        return False

    def sol(level) -> bool:
        return sum == n

    def printf(level):
        global sum
        for i in range(1, level+1):
            print(stack[i], end = " ")
        print()
        sum -= stack[level]

    def solve(level):
        init(level)
        while succ(level) is True:
            if valid(level) == True:
                if sol(level) == True:
                    printf(level)
                else:
                    solve(level+1)
    solve(1)
partition()
