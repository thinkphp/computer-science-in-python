def fn():
    def part(lo,hi):
        j = lo - 1
        piv = arr[hi]
        for i in range(lo, hi+1):
            if arr[i]<=piv:
                j+=1
                arr[j],arr[i]=arr[i],arr[j]
        return j

    def quicksort(lo,hi):
        piv = part(lo,hi)
        if lo < piv - 1:
            quicksort(lo, piv - 1)
        if piv + 1 < hi:
            quicksort(piv + 1, hi)

    def select(k,lo,hi):
        piv = part(lo,hi)
        if piv == k-1:
            return arr[piv]
        elif k-1>piv:
            return select(k,piv+1,hi)
        return select(k,lo,piv-1)

    arr = [14,4,5,21,3,33,23]
    n = len(arr)
    print(arr)
    for i in range(n):
        print("%d => %d"%(i+1,select(i+1,0,n-1)))
    quicksort(0, n-1)
    print(arr)
fn()
