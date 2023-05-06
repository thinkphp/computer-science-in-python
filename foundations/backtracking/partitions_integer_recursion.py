def fn():
    global g
    f = open("partitiinumar.in","r")
    g = open("partitiinumar.out","w")
    def solve(level):
       global sum, g
       if sum == n:
           for i in range(1, level):
               g.write(str(stack[i]))
               g.write(" ")
           g.write("\n")
       else:
           if level == 1:
              stack[level] = 0
           else:
              stack[level] = stack[level-1]-1
           while stack[level]+sum<n:
               stack[level]+=1
               sum += stack[level]
               solve(level+1)
               sum -= stack[level]

    global sum
    n = int(f.readline())
    stack = [0] * (n+1)
    sum = 0
    solve(1)
fn()
