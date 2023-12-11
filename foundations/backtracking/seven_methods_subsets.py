# Generating the subsets of a Set = { 1, 2, 3 }
# Sonata Alla Turca no 11 in A major K 331
def main():
    n = 3
    stack = [0] * (n+1);
    stack2 = [0] * (n+1)

    #method 0 using Backtracking iteratively
    def init():
        stack2[summit] = -1

    def succ():
        if stack2[ summit ] < 1:
            stack2[ summit ]+=1
            return 1
        return 0

    def valid():
        return 1

    def sol():
        return summit == n

    def print_solution():
        for i in range( 1, n + 1 ):
            if stack2[ i ] == 1:
                print(i, end=" ")
        print()

    def bk():
        global summit
        summit = 1
        init()

        while summit > 0:

            s = 1
            v = 0
            while s and v == 0:
                s = succ()
                if s:
                    v = valid()
            if s:
                if sol() is True:
                    print_solution()
                else:
                    summit+=1
                    init()
            else:
                summit-=1

    print("method#0 Backtracking iterative")
    bk()

    def solution(k):
        for i in range(1, k+1):
            print(stack[i], end = " ")
        print()

    #method 1 using Backtracking recursively
    def subsets(k):
        if k<=n:
            for i in range(stack[k-1]+1, n+1):
                stack[k] = i
                solution( k )
                subsets( k + 1 )

    print("Method#1 Backtracking recursive")
    subsets(1)

    #method 2 based on Bitwise
    def subsets_bitwise(n):
        size = 2**n
        mask = 1
        print("Subsets(%d) = ( "%n,end="")
        for i in range(1, size):
            print("{", end="")
            for j in range(0, n):
                if (mask<<j)&i:
                    print(j+1, end =",")
            print("\b}", end=" ")
        print(")")
    print("method#3 Bitwise")
    subsets_bitwise(5)

    #method 3 based on Elegant List Comprehension
    def subsets_elegant( working_set, level, n ):
        if level == n:
            sol = [k for k in working_set if working_set[k] == 1]
            print(sol)
        else:
            level+=1
            for i in [0,1]:
                working_set[level] = i
                subsets_elegant(working_set, level, n)
    print("method#4 (Elegant List Comprehensive)")
    subsets_elegant({},0,n)
main()

def gen_sub():
    n = 3
    vec = [0] * (n)
    s = 0

    while not (s == n):
        vec[n-1]+=1
        for i in range(n-1,-1,-1):
            if vec[i] > 1:
                vec[i-1] += 1
                vec[i] = 0
        s = 0
        for i in range(0,n):
            if vec[i]:
                print(i+1, end= " ")
            s += vec[i]
        print()

print("method#5 Binary Addition")
gen_sub()

def gen_subsets_stack():
    stack = []
    n = 3
    stack.append(1)
    while len(stack)>0:
        print(stack)
        if stack[-1] < n:
            stack.append(stack[-1]+1)
        else:
            stack.pop()
            if len(stack)>0:
                stack[-1]+=1

print("method#6 Generating Subsets using a Stack")
gen_subsets_stack()

print("method#7 Bk Rec")
def gen_subsets_bk_rec():
    n = 3
    stack = [ 0 ] * (n+1)
    def init(k):
        stack[k]=-1
    def succ(k):
        if stack[k]<1:
            stack[k]+=1
            return 1
        return 0
    def sol(k):
        return k == n
    def printf(k):
        for i in range(1, n+1):
            if stack[i] == 1:
                print(i, end = " ")
        print()

    def bk(k):
        init(k)
        while succ(k):
            if sol(k):
                printf(k)
            else:
                bk(k+1)
    bk( 1 )

gen_subsets_bk_rec()
