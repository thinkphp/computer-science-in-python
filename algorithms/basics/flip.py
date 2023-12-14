def main():
    #fin = open("flip.in","r")
    #nm = [int(i) for i in fin.readline().split()]
    nm = [int(i) for i in input().split()]
    n = nm[0]
    m = nm[1]
    matrix = [list(map(int, input().split())) for _ in range(n)]
    #print(matrix)
    sum_max = 0
 
    def solve_flip(stack):
 
        #declare the variable as nonlocal to modify the outer variable
        nonlocal sum_max
        #declare a variable that holds local stotal
        stotal = 0
        #make a copy of the matrix
        matrix2 = [row[:] for row in matrix]
 
        for line in stack:
            for j in range(m):
                matrix2[line][j] *= -1
 
        for j in range(m):
            s = 0
            for i in range(n):
                s += matrix2[i][j]
            if s<0:
               s *= -1
            stotal += s
 
        if sum_max < stotal:
            sum_max = stotal
 
    size = 2**n
    mask = 1
    for i in range(1,size):
        #empty stack
        stack = []
        for j in range(n):
            if (mask<<j)&i:
                #print(j, end = " ")
                stack.append(j)
        solve_flip(stack)
    #fout = open("flip.out","w")
    print(sum_max)
    #fout.write(str(sum_max))
main()
