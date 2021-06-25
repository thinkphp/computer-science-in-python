def selectByMin(arr):
    n = len(arr)
    for i in range(0, n-1):
        k = i
        min = arr[i]
        for j in range(i + 1, n):
            if arr[j] < min:
               min = arr[j]
               k = j
        if i != k:
           arr[k], arr[i] = arr[i], arr[k]

def main():
    arr = [9,8,7,6,5,44,2020,2021,-1,0,11,10]
    print(arr)
    selectByMin(arr)
    print(arr)
main()
