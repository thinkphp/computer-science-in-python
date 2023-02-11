def _qs(lo, hi, arr):

    i = lo
    j = hi
    middle = arr[(lo + hi)>>1]

    while i <= j:

        while arr[i] < middle:
            i += 1
        while arr[j] > middle:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if lo < j:
        _qs(lo, j, arr)
    if i < hi:
        _qs(i, hi, arr)            

def qs(arr):

    _qs(0, len(arr) - 1, arr)

def func():

    arr = [4,54,7,8,9,10,-1]

    print(arr)

    qs( arr )

    print( arr )

func()
