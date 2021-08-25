def main():
    arr = [5,90,23,3,2,-1,100,-2]
    n = len(arr)
    B = [0] * (n + 1)
    C = [0] * (n + 1)
    for i in range(0, n):
        C[i] = arr[i]

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                B[j] += 1
            else:
                B[i] += 1
    for i in range(0, n):
        arr[B[i]] = C[i]

    print(arr)
main()
