#
# Dynamic Programming
#
def find_lis(arr):

    n = len( arr )

    best = [0] * (n)
    best[n-1] = 1

    # we will create the best array
    for i in range(n-2, -1, -1):
        aux = arr[i]
        max = 0
        for j in range(i+1, n):
            if arr[j] > aux and best[j] > max:
                max = best[j]
        best[i] = 1 + max
    maxBest = best[0]
    posMax = 0
    for i in range(1, n):
        if best[i]>maxBest:
            maxBest = best[i]
            posMax = i
    print(best)
    print(maxBest, posMax)
    print(arr[posMax], end = " ")
    pos = maxBest
    pos-=1
    for i in range(posMax+1, n):
        if best[i] == pos and arr[i] > arr[posMax]:
            print(arr[i], end = " ")
            pos-=1

def gokyo():

    arr = [24,12,15,15,19]
    print(arr)
    find_lis(arr)

gokyo()
