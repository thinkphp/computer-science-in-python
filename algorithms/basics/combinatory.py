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
