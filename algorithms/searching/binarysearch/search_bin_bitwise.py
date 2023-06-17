def fn():
    arr = [-1,30,35,37,45,50,55]
    n = len(arr)
    pow = 1
    while pow<n:
        pow<<=1
    key = 45
    index = 0
    while pow:
       if (index+pow) < n and arr[index+pow]<=key:
          index = index + pow
       pow >>= 1
    if arr[index] == key:
        print(index)
    else:
        print("Not Found")
fn()
