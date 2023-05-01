#
# Lecture Notes: Backtracking.
#
# Elements of combinatorics.
#
# Permutation.
# Combinations.
# Arrangements.
# Partitions Set.
# Partitions Integer.
# Subsets.
#
# Product Cartesian MxM.
# Product Cartesian AxBx..xZ.
def perm1(n):
    def ok(level):
        for i in range(1, level):
            if stack[level] == stack[i]:
                return False
        return True
    def back(level):
        if level == n+1:
            print(stack)
        else:
            for i in range(1, n+1):
                stack[level] = i
                if ok(level):
                    back(level+1)
    n = n
    stack = [0] * (n+1)
    back(1)
perm1(4)

print("Permutations2:")
def perm():
    def accepted(level):
        for i in range(1, level):
            if stack[i] == stack[level]:
                return False
        return True
    def solve(level):
        for i in range(1, n+1):
            stack[level] = i
            if accepted(level) is True:
               if level == n:
                  for i in range(1,n+1):
                      print(stack[i], end=" ")
                  print()
               else:
                  solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)
perm()

print("Combinations:")
print()

def comb(n,k):
    def accepted(level):
        for i in range(1, level):
            if stack[i] == stack[level]:
                return False
        return True
    def solve(level):
        for i in range(stack[level-1]+1, n+1):
            stack[level] = i
            if accepted(level) is True:
               if level == k:
                  for i in range(1,k+1):
                      print(stack[i], end=" ")
                  print()
               else:
                  solve(level+1)
    n = n
    k = k
    stack = [0] * (n+1)
    solve(1)
comb(4,2)

print()

print("Arrangements:")
def arrange(n,k):
    def accepted(level):
        for i in range(1, level):
            if stack[i] == stack[level]:
                return False
        return True
    def solve(level):
        for i in range(1, n+1):
            stack[level] = i
            if accepted(level) is True:
               if level == k:
                  for i in range(1,k+1):
                      print(stack[i], end=" ")
                  print()
               else:
                  solve(level+1)
    n = n
    k = k
    stack = [0] * (n+1)
    solve(1)
arrange(4,2)

print()

print("Partitions of a set")
def partSet():
    def getMax(level):
        max = 0
        for i in range(1, level):
            if stack[i]>max:
                max = stack[i]
        return max
    def display_solution():
        max = getMax(n+1)
        for i in range(1, max+1):
            for j in range(1,n+1):
                if stack[j]==i:
                    print(j, end="")
            print("*", end="")
        print()
    def solve(level):
        for i in range(1, getMax(level)+1+1):
            stack[level] = i
            if level == n:
                display_solution()
            else:
                solve(level+1)

    n = 3
    stack = [0] * (n+1)
    solve(1)
partSet()

print()
print("Partitions of an integer")
def partInt():
    def solve(level):
        global sum
        if sum == n:
            for i in range(1, level):
                print(stack[i], end=" ")
            print()
        else:
            stack[level] = 0
            while stack[level]+sum<n:
                stack[level]+=1
                sum += stack[level]
                solve(level+1)
                sum -= stack[level]

    n = 3
    global sum
    sum = 0
    stack = [0] * (n+1)
    solve(1)
partInt()

print()
print("Subsets")
def subsets(k):
    def solution(level):
        for i in range(1,level+1):
            print(stack[i], end=" ")
        print()
    def solve(level):
        if level<=n:
            for i in range(stack[level-1]+1, n+1):
                stack[level] = i
                solution(level)
                solve(level+1)
    n = k
    stack = [0] * (n+1)
    solve(1)
subsets(3)

print("Product Cartesian")

def Cartesian(k):
    def solve(level):
        if level == 3:
            print("(",end="")
            for i in range(1, 3):
                print(stack[i], end=",")
            print("\b)",end="")

        else:
            for i in range(1, m+1):
                stack[level] = i
                solve(level+1)
    m = k
    stack = [0] * (m+1)
    print("{",end="")
    solve(1)
    print("}")

Cartesian(5)

print("Product Cartesian AxB")

def CartesianAB(a,b):
    def solve(level):
        if level == n+1:
            print("(",end="")
            for i in range(1, n+1):
                print(stack[i], end=",")
            print("\b)",end="")

        else:
            stack[level] = 0
            while stack[level]<M[level]:
                stack[level]+=1
                solve(level+1)
    M = [0,a,b]
    n = len(M)-1
    stack = [0] * (n+1)
    print("{",end="")
    solve(1)
    print("}")

CartesianAB( 2, 3 )

def fn():
    def subsets(working_set, level, n):
        if level == n:
            s = {i for i in working_set if working_set[i] == 1}
            solutions.append(s)
        else:
            level+=1
            for i in [0,1]:
                working_set[level] = i
                subsets(working_set,level,n)
    n = 3
    solutions = []
    subsets({},0,n)
    print(solutions)
fn()
