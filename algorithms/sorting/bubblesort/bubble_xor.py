def bubblesort(arr):
  n = len(arr)
  finished = 0
  while finished != 1:
    swapped = False
    for i in range(0, n - 1):
      if arr[i] > arr[i + 1]:
        swapped = True
        xor = arr[i] ^ arr[i + 1]
        arr[i] = xor ^ arr[i]
        arr[i + 1] = xor ^ arr[i]
    if swapped is True:
      n -= 1
    else:
      finished = 1
def func():
  arr = [73, 2, 3, 4, 5, 7, -8, 0]
  print(arr)
  bubblesort(arr)
  print(arr)
func()
