def _QuickSort(arr, low, high):

    pivot_index = (low + high) >>1
    
    pivot_value = arr[ pivot_index ]
    
    i = low
    
    j = high

    while i <= j:

        while arr[i] > pivot_value:
            i += 1

        while arr[j] < pivot_value:
            j -= 1

        if i <= j:
           arr[i], arr[j] = arr[j], arr[i]
           i+=1
           j-=1

    if low < j:
        _QuickSort(arr, low, j)
        
    if i < high:
        _QuickSort(arr, i, high)

# Example usage:
#my_array = [3, -1, 4, 1, 5, 9, 2, 6, -59, -333, 5]

f = open("algsort.in","r")

n = int(f.readline().strip())

my_array = [int(i) for i in f.readline().split()]

_QuickSort(my_array, 0, len(my_array) - 1)

arr_of_string = map(str,my_array)

arr_of_string = " ".join(arr_of_string)

with open("algsort.out","w") as file:

        file.write(arr_of_string)
