
#
# We consider N (N<=1000) types of banknotes, of different values,
# of each there being an unlimited number of pieces. Determine a payment
# method of payment, of value S using a minimum numbers of banknotes.
#
# Input:
# N = 5
# S = 100
#         3,15,1,5,2
#
# Output: 6 * 15
#         2 * 5

def fn():
    def sorting(sign):
        n = len(B)
        for i in range(1, n):
            j = i - 1
            aux = B[i]
            while j >= 0 and B[j]*sign>aux*sign:
                B[j+1] = B[j]
                j-=1
            B[j+1] = aux

    def solve():
        global S
        sorting(-1)
        for i in B:
            if S>=i:
               print("%d * %d"%(S//i,i))
            S-=(S//i)*i
            if S == 0:
                break
        if S>0:
            print("No Solution")
    global S
    N = int(input("N="))
    S = int(input("S="))
    B = [0]*(N)
    for i in range(0, N):
        B[i] = int(input())
    solve()
fn()
