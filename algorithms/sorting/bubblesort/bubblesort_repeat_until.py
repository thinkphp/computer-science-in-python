#
# Bubble Sort Technique made easy with 
# the structure Repeat ... Until
#
def BubbleSort(arr):
    finished = 0
    swapped = 0
    l = len(arr)
    print l
    while not finished == 1:
          swapped = 0
          i = 0
          while i <= l - 2:
          	    if arr[i] > arr[i+1]:
          	       holder = arr[i]
          	       arr[i] = arr[i+1]
          	       arr[i+1] = holder	 
          	       swapped = 1
          	    i = i + 1
          if swapped:
          	 l = l - 1
          else:
             finished = 1 	 
    print arr         
          	 

BubbleSort([9,8,7,6,5,4,3,2,1,0])          	
             
