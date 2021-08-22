def main():
    arr = [9,8,7,6,5,4,3,2,-11]
    print(arr)
    n = len(arr)
    i = 1
    while i < n and arr[i] == arr[0]:
        i +=1
    if i < n:
      if arr[i - 1] < arr[ i ]:
            flag = True
            for j in range(i , n - 1):
                if arr[j] > arr[j+1]:
                    flag = False
            if flag is True:
               print("Vector crescator!")
            else:
               print("Vector neordonat!")
 
      elif arr[i - 1] > arr[ i ]:
            flag = True
            for j in range(i, n - 1):
                if arr[j] < arr[j+1]:
                    flag = False
            if flag is True:
                print("Vector descrescator!")
            else:
                print("Vector neordonat!")
    else:
        print("Constant Vector!")
 
main()
