def fn():
    def part(lo,hi):
        j = lo - 1
        piv = arr[hi]
        for i in range(lo,hi+1):
            if arr[i]<=piv:
                j+=1
                arr[j],arr[i] = arr[i],arr[j]
        return j
    def sel(k,lo,hi):
        piv = part(lo,hi)
        if piv == k-1:
            return arr[piv]
        elif piv < k - 1:
            return sel(k,piv+1,hi)
        else:
            return sel(k,lo,piv-1)
    arr = [17,20,4,7,101,11,201]
    print(arr)
    k = 7
    ans = sel(k,0,len(arr)-1)
    print("On position %d is %d"%(k,ans))
    arr.sort()
    print(arr)
fn()
