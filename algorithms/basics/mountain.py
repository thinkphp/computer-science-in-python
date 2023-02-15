def analysis(arr):

    n = len(arr)
    i = 1
    while i < n and arr[i] > arr[i-1]:
        i+=1
    print(i)    
    if i == 1 or i == n:
        print("Not Found Mountain!")

    if i < n:
        if arr[i] < arr[i-1]:
            descend = True
            for j in range(i, n):
                if arr[j] > arr[j-1]:
                    descend = False
                    break
            if descend is True:
                print("Mountain!")
            else:
                print("Not Found Mountain!")

def mountain():

    arr = [1,2,3,4,5,4,3,2]
    arr = [1,2,3,4,5,4,3,2,-7]
    arr = [7,7,7,7,7,7,7]

    analysis(arr)

mountain()
