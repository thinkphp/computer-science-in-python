'''
Author:
Adrian Statescu

Description:
Counting Sorting Algorithm

References:
https://w...content-available-to-author-only...s.eu/algorithms/counting-sort/#Counting_Sort_Algorithm_-_Phase_2_Counting_the_Elements

'''
def FindMinMax(arr, n):
    min = arr[0]
    max = arr[0]
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return min, max
def main():

    arr = [9, 8, 7, 6, 5, -4, 3, -2, 1, 0, -4, -5, -4, -1, -8, -19, -19, 8]
    n = len(arr)
    print(arr)

    min, max = FindMinMax(arr, n)

    counts = [0] * (max - min + 10)

    for i in range(0, n):
        counts[arr[i] - min] += 1

    pos = 0
    for i in range(0, max - min + 1):
        for j in range(0, counts[i]):
            arr[pos] = i + min
            pos += 1

    print(arr)

main()
