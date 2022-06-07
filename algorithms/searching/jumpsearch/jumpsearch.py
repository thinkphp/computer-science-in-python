import math
 
def jumpsearch(arr, key):
 
    n = len(arr)
 
    lo = 0
 
    jump = int(math.sqrt(n))
 
    hi = jump
 
    while hi < n and arr[hi] <= key:
 
          lo = hi
 
          hi += jump
 
          if hi > n + 1:
 
             hi = n
 
    found = False
 
    for i in range(lo, hi):
 
        if arr[i] == key:
 
            print("The element %d is found at index: %d" % (key, i))
 
            found = True
 
    if found is False:
 
        print("Not Found")
 
def main():
 
    # define an array in sorted order
    arr = [30, 40, 50, 55, 190, 200, 300, 350]
 
    # define an array of tests
    tests = [30, 40, 5, 55, 10, 200, 300, 350, 201]
 
    for k in tests:
        jumpsearch(arr, k)
 
main()
