def searchbin(lo, hi, arr, key):
    if lo > hi:
        return -1
    else:
        m = (lo + hi) // 2
        if key == arr[m]:
            return m + 1
        if key < arr[m]:
            return searchbin(lo, m - 1, arr, key)
        else:
            return searchbin(m + 1, hi, arr, key)
def sort(arr, n):
    lo = 0
    hi = n - 1
    for i in range(1, n):
        lo = 0
        hi = i -1
        holder = arr[i]
        while lo <= hi:
            m = (lo + hi) // 2
            if holder < arr[m]:
                hi = m - 1
            else:
                lo = m + 1
        for k in range(i-1, lo-1, -1):
            arr[k+1] = arr[k]
        arr[lo] = holder
def main():
    file = open("searchbin.in","r")
    n = int(file.readline().strip())
    data = file.readline().strip().split(" ")
    arr = [int(x) for x in data]
    print(arr)
    dic = {}
    for i in range(0, n):
        dic.update({arr[i]: i + 1})
    sort(arr, n)
    key = int(input("key = "))
    ans = searchbin(0, n - 1, arr, key)
    if ans == -1:
        print("Not Found!")
    else:
        print("Found on position: ", dic[key])
main()
