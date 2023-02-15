
def binary_search_rec(lo, hi, arr, search):

    if lo > hi:
        return -1

    m = (lo + hi) >> 1

    if arr[m] < search:

        return binary_search_rec(m + 1, hi, arr, search)

    elif arr[m] > search:

        return binary_search_rec(lo, m - 1, arr, search)

    else:

        return m

def binary_search2(arr, search):

    return binary_search_rec(0, len(arr)-1, arr, search)

def binary_search(arr, search):

    lo = 0
    hi = len(arr) - 1
    pos = -1

    while lo <= hi:
        #print("[%d,%d]" % (lo,hi))
        m = (lo + hi) >> 1
        if search > arr[m]:
            lo = m + 1
        elif search < arr[m]:
            hi = m - 1
        else:
            return m

    return pos

def func():
    arr = [11,41,51,61,71,81,91,101]
    tests = [11, 51, 10, 20, 30, 40, 81, 101]
    print(arr)
    for search in tests:
        pos = binary_search(arr, search)
        if pos != -1:
           print("%d lies on position: %d"%(search, pos))
        else:
           print("%d: Not Found" % search)
func()
