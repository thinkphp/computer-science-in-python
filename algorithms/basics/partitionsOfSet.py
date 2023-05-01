def fn():
    def maxim(level):
        max = 0
        for i in range(1, level):
            if stack[i] > max:
                max = stack[i]
        return max
    def display(level):
        global fout
        maxi = maxim(n+1)
        for i in range(1, maxi+1):
            for j in range(1, n+1):
                if stack[j] == i:
                    print(j, end ="")
                    #fout.write(str(j))
            print("*", end="")
            #fout.write("*")
        print()
        #fout.write("\n")
 
    def solve(level):
        for i in range(1, maxim(level)+1+1):
            stack[level] = i
            if level == n:
                display(level)
            else:
                solve(level+1)
    global fout
    #fin = open("partitiimultime.in","r")
    #fout = open("partitiimultime.out","w")
    #n = int(fin.readline())
    n = int(input())
    stack = [0] * (n+1)
    stack[1] = 1
    solve(2)
fn()
