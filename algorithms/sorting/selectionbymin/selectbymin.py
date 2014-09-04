from random import shuffle
def selectbymin(arr):
    n = len(arr)
    for i in range(0,n-1):
        k = i
        for j in range(i+1,n):
            if arr[j] < arr[k]:
               k = j
        arr[i],arr[k] = arr[k],arr[i]
    return None
vec = range(20)
arr = vec[:]
shuffle(arr)
print "Input:"
print arr
selectbymin(arr)
print "Sorted:"
print arr    
