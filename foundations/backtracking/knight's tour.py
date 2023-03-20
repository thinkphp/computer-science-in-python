import sys
def func():
    global cnt
    cnt = 1
    x = [-1, 1, 2, 2, 1, -1, -2,-2]
    y = [ 2, 2, 1,-1,-2, -2, -1, 1]
 
    def knight(level, row, col) -> None:
         global cnt
         if level == n * n:
            for i in range(1, level):
                print("[%d,%d]"%(matrix[i][0], matrix[i][1]), end = " ")
            print("[%d,%d]"%(matrix[row][0], matrix[col][1]))
            cnt = 1
            for i in range(1, level):
                sols[ matrix[i][0] ][ matrix[i][1] ] = cnt
                cnt+=1
            sols[row][col] = cnt    
            for i in range(1, n+1):
                for j in range(1, n+1):
                    print(sols[i][j], end =" ")
                print()
 
            sys.exit()
         else:
            matrix[level][0] = row
            matrix[level][1] = col
            for i in range(0, 8):
                l = row + x[i]
                c = col + y[i]
                if l >= 1 and l <= n and c >= 1 and c <= n and explored[l][c] == 0:
                   explored[l][c] = 1
                   knight(level+1, l, c)
                   explored[l][c] = 0
    n = 6
    DIM = 100
    matrix = [[0 for j in range(3)] for i in range(DIM)]
    explored = [[0 for j in range(DIM)] for i in range(DIM)]
    sols = [[0 for j in range(n+1)] for i in range(n+1)]
    knight(1,1,1)
func()
