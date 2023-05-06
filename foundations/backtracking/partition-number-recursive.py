def partition():
    def solve(level):
        global sum
        if sum == n:
            for i in range(1, level):
                print(stack[i], end = " ")
            print()
        else:
             if level == 1:
                    stack[level] = 0
             else:
                 stack[level] = stack[level-1]-1
             while stack[level] + sum < n:
                stack[level] += 1
                sum += stack[level]
                solve(level+1)
                sum -= stack[level]
    global sum
    n = 3
    stack = [0] * (n+1)
    sum = 0
    solve(1)

partition()

def func2():

    def accepted(level):
        for i in range(1, level):
            if stack[level] == stack[i]:
                return False
        return True

    def solve(level):
        if level == k + 1:
            for i in range(1, k+1):
                print(stack[i], end = " ")
            print()
        else:
            for i in range(1, n + 1):
                stack[level] = i
                if accepted(level):
                   solve(level+1)
    n = 3
    k = 2
    stack = [0] * (n+1)
    solve(1)
func2()

def func():
    def subsets(working_set, level, n):
        if level == n:
            s = {k for k in working_set if working_set[k] == 1}
            print(s)
        else:
            level += 1
            for i in [0,1]:
                working_set[level] = i
                subsets(working_set, level, n)
    def solution(level):
        for i in range(1, level+1):
            print(stack[i], end = " ")
        print()
    def solve(level):
        if level <= n:
            for i in range(stack[level-1]+1, n+1):
                stack[level] = i
                solution(level)
                solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)
    subsets({},0,n)
func()
