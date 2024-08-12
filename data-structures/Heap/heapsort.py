def main():
    n = int(input("N="))
    arr = [0] + list(map(int, input().split(" ")))  # Start indexing from 1 by adding a dummy 0 element

    def getIndMin(i, n):
        left = 2 * i
        right = 2 * i + 1
        # If both left and right children exist
        if right <= n:
            if arr[right] < arr[left]:
                return right
            else:
                return left
        # If only the left child exists
        if left <= n:
            return left
        else:
            return i  # No valid child, return the current index

    def heapify(i, n):
        while i <= n // 2:
            ind = getIndMin(i, n)
            if arr[i] <= arr[ind]:
                break
            arr[i], arr[ind] = arr[ind], arr[i]
            i = ind

    def minHeap():
        for i in range(n // 2, 0, -1):
            heapify(i, n)
    def heapsort():
        minHeap()
        for i in range(n,0,-1):
            aux = arr[1]
            arr[1] = arr[i]
            arr[i] = aux
            heapify(1, i-1)

    print("Original array:", arr[1:])
    #minHeap()
    #print("Min-heap:", arr[1:])
    heapsort()
    print("Sorted array:", arr[1:])

main()
