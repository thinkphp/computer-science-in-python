NOT_FOUND = -1

def binary_search2(arr, lo, hi, key) -> int:

    while lo <= hi:
        m = (lo + hi)>>1
        if arr[m] < key:
            lo = m + 1
        elif arr[m] > key:
            hi = m - 1
        else:
            return m
    return NOT_FOUND

def binary_search(arr, lo, hi, key) -> int:

    if lo > hi:

        return NOT_FOUND
    else:
        m = (lo+hi)//2
        if key > arr[m]:
            return binary_search(arr, m+1, hi, key)
        elif key < arr[m]:
            return binary_search(arr, lo, m-1,key)
        else:
            return m
def fn():
    arr = [10,21,31,41,51,55,71]
    key = 41
    print(arr)
    search = binary_search2(arr, 0, len(arr)-1, key)
    print(search)
fn()
