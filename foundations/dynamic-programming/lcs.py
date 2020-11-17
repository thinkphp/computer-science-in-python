import sys

def main():
    x = [0,1,5,7,5,4]
    y = [0,2,1,2,3,4,5,2,7]
    n, m = len(x), len(y)
    lcs = [ [0 for i in range(m)] for j in range(n) ]

    #for debug
    #print lcs
    
    for i in range(1,n):
        for j in range(1, m):
            if x[i] == y[j]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
    print lcs[n-1][m-1]

    i = n - 1
    j = m - 1
    ans = []

    while i != 0 and j!= 0:
        if(x[i] == y[j]):
           ans.append(x[i])
           i = i - 1
           j = j - 1
        else:
            if lcs[i][j-1] < lcs[i-1][j]:
                i = i - 1
            else:
                j = j - 1
    while len(ans) != 0:          
          x = ans.pop()
          sys.stdout.write(str(x) + " ")

    print ""
            
main()
