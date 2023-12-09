def partition(arr, low, high):
    pivot_index = (low + high) >>1
    pivot_value = arr[pivot_index]
 
    i = low - 1
    j = high + 1
 
    while True:
        i += 1
        while arr[i] < pivot_value:
            i += 1
 
        j -= 1
        while arr[j] > pivot_value:
            j -= 1
 
        if i >= j:
            return j
 
        # Swap elements at positions i and j
        arr[i], arr[j] = arr[j], arr[i]
 
def quicksort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quicksort(arr, low, partition_index)
        quicksort(arr, partition_index + 1, high)
 
# Example usage:
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quicksort(my_array, 0, len(my_array) - 1)
print(my_array)
