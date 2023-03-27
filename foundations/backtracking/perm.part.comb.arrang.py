import numpy as np
##
## Partitions: numbers and sets.
## Arrangements.
## Combinations.
## Permutations.
## Subsets.
##

# iteratively variant
def partitionNum():
    def init():
        stack[level] = 0
    def succ():
        global sum
        if stack[level] < n - sum:
            stack[level] += 1
            return True
        else:
            sum -= stack[level-1]

    def valid():
        global sum
        if stack[level] <= n - sum:
           sum += stack[level]
           return True
        return False

    def sol():
        return sum == n

    def printf():
        global sum
        for i in range(1,level+1):
            print(stack[i], end = " ")
        print()
        sum -= stack[level]

    def solve():
        global level
        level = 1
        init()
        while level > 0:
            s = True
            v = False
            while s and not v:
                s = succ()
                if s:
                    v = valid()
            if s:
                if sol():
                    printf()
                else:
                    level +=1
                    init()
            else:
                level -= 1
    global sum
    sum = 0
    n = 3
    stack = [0] * (n+1)
    solve()

partitionNum()

print()

def partitionSet():

    def init(level):
        stack[level] = 0

    def succ(level):
        if stack[level] < stack[level-1] + 1:
            stack[level] += 1
            return True
        return False

    def valid(level):
        return True

    def sol(level):
        return level == n

    def printf(level):
        maxv = np.max(stack)
        for i in range(1, maxv+1):
            print("{", end="")
            for k in range(1, n+1):
                if i == stack[k]:
                    print(k, end = ",")
            print("\b}", end="")
        print()

    def solve(level):
        init(level)
        while succ(level):
            if valid(level):
                if sol(level):
                    printf(level)
                else:
                    solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)

partitionSet()

print()

def arrange():
    def ok(level):
        for i in range(1, level):
            if stack[level] == stack[i]:
                return False
        return True

    def solve(level):
        if level == k + 1:
            for i in range(1, k + 1):
                print(stack[i], end = " ")
            print()
        else:
            for i in range(1, n + 1):
                stack[level] = i
                if ok(level):
                    solve(level+1)
    n = 3
    k = 2
    stack = [0] * (n+1)
    solve(1)
arrange()

def comb():
    def ok(level):
        for i in range(1, level):
            if stack[level] == stack[i]:
                return False
        return True

    def solve(level):
        if level == k + 1:
            for i in range(1, k + 1):
                print(stack[i], end = " ")
            print()
        else:
            for i in range(stack[level-1]+1, n + 1):
                stack[level] = i
                if ok(level):
                    solve(level+1)
    n = 3
    k = 2
    stack = [0] * (n+1)
    solve(1)
comb()


def perm():
    def ok(level):
        for i in range(1, level):
            if stack[level] == stack[i]:
                return False
        return True

    def solve(level):
        if level == n + 1:
            for i in range(1, n + 1):
                print(stack[i], end = " ")
            print()
        else:
            for i in range(1, n + 1):
                stack[level] = i
                if ok(level):
                    solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)
perm()

def _subsets():
    def solve(level):
        if level <= n:
            for i in range(stack[level-1]+1, n+1):
                stack[level] = i
                for i in range(1,level+1):
                    print(stack[i], end=" ")
                print()
                solve(level+1)

    n = 3
    stack = [0] * (n+1)
    solve(1)
_subsets()

def subsets():
    def solve(working_set, level, n):
        if level == n:
            s = {k for k in working_set if working_set[k] == 1}
            solutions.append(s)
        else:
            level += 1
            for i in [0,1]:
                working_set[level] = i
                solve(working_set, level, n)
    n = 3
    solutions = []
    solve({}, 0, n)
    print(solutions)
subsets()
