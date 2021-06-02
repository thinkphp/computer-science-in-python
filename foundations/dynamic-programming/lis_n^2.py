# Longest Increasing Subsequence
# Time complexity: O(n^2)
# Solved using Decorator

def read( f ):
    file = open("scmax.in","r")
    n = int(file.readline().split("\n")[0])
    V = [int(x) for x in file.readline().split(" ")]
    return f(n,V)

@read
def solve(n, V):
    file = open("scmax.out","w")
    L = [1] * (n + 1)
    L[1] = 1
    print(V)
    for i in range(n - 2, -1, -1):
        max = 0
        for j in range(i+1, n):
            if V[j] > V[i] and L[j] > max:
                max = L[j]
        L[i] = 1+ max
    print(L)
    max = L[0]
    pos = -1
    for i in range(1,n):
        if L[i] > max:
           pos = i
           max = L[i]
    file.write(str(max) + "\n")
    print(max, end = "\n")
    file.write(str(V[pos]) + " ")
    print(V[pos],end=" ")
    i = pos + 1
    while i < n:
         if V[i] > V[pos] and L[i] == max - 1:
            file.write(str(V[i]) + " ")
            print(V[i], end =" ")
            max -= 1
         i +=1
    print("\nSolved!")
