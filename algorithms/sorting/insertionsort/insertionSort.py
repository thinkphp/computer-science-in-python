def insertionSort(arr):

    n = len(arr) #getting the length of the array

    for i in range(1,n): #for each item do

        temp = arr[i]
        j = i - 1

        while j>=0 and arr[j] > temp:

              arr[j+1] = arr[j]
              j = j - 1

        arr[j+1] = temp

    return arr 

def insertionSort2(arr):
    
    n = len(arr) #getting the length of the array

    for i in range(1,n):

        temp = arr[i]

        for j in range(i-1,-2,-1):

            if(arr[j] > temp):

               arr[j+1] = arr[j]
            else:
               break
            
        arr[j+1] = temp 

    return arr 

def insertionSortModified(arr):

    n = len(arr)

    for i in range(1,n):

        temp = arr[i]
 
        li = 0
        ls = i-1

        while li<=ls:

           m = (li+ls)/2

           if arr[m] > temp:
              ls = m - 1
           else:
              li = m + 1 

        for j in range(i-1,li-1,-1):
            arr[j+1] = arr[j]

        arr[li] = temp

    return arr

arr = [9,8,7,6,5,4,3,2,1,0,-33,11,33]

print insertionSort2(arr)
