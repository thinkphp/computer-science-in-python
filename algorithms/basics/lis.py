def lis(arr):
    n = len(arr)
    best = [0] * (n)
    best[n-1] = 1
    for i in range(n-2,-1,-1):
        max = 0
        temp = arr[i]
        for k in range(i+1, n):
            if arr[k]>=temp and best[k]>max:
                max = best[k]
        best[i] = 1 + max
    print(best)
    pos = 0
    max = best[0]
    for k in range(1,n):
        if best[k]>max:
            max = best[i]
            pos = k+1
    print(arr[pos], end = " ")
    k = pos
    ln = best[pos]
    ln-=1
    for i in range(k, n):
        if best[i] == ln and arr[i] > arr[k]:
           print(arr[i], end = " ")
           ln-=1

def func():
    arr = [0,-1,31,2,41,511,72,17]
    print(arr)
    lis(arr)
func()
