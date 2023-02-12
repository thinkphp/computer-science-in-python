def merge(lo,m,hi,arr):

    i = lo
    j = m + 1

    aux = []
    while i <= m and j <= hi:

        if arr[i] < arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1
    while i <= m:
        aux.append(arr[i])
        i+=1

    while j <= hi:
        aux.append(arr[j])
        j +=1

    k = 0
    for i in range(lo, hi+1):
        arr[i] = aux[k]
        k +=1


def mergesort(lo, hi, arr):

    if lo < hi:
        m = (lo + hi) >> 1
        mergesort(lo, m, arr)
        mergesort(m + 1, hi, arr)
        merge(lo, m, hi, arr)

def sort(arr):

    n = len(arr)

    mergesort(0, n - 1, arr)

def func():

    arr = [9,-8,-7,6,0,-95,4,3,2]

    print( arr )

    sort(arr)

    print(arr)

func()
