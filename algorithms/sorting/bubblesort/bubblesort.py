from random import shuffle

def bubblesort(arr):

    swapped = True
    n = len(arr)-1

    while swapped:
          swapped = False
          for i in xrange(n):
              if arr[i] > arr[i+1]:
                 arr[i], arr[i+1] = arr[i+1], arr[i]  
                 swapped = True          
    return None

def bubblesort2(arr):
    n = len(arr)-1;
    
    for i in range(0,n):
        for j in range(n,i,-1):
            if arr[j] < arr[j-1]:
               arr[j],arr[j-1] = arr[j-1], arr[j]    
                    
    return None

def bubblesort3(arr):
    n = len(arr)-1;   
    for i in range(n,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
               arr[j],arr[j+1] = arr[j+1], arr[j]    
                    
    return None

if __name__ == "__main__":

    vec = range(10)
    arr = vec[:]
    shuffle(arr)
    print 'Input array'
    print arr
    print 'sorted array'
    bubblesort3(arr)
    print arr