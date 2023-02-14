#
# Shell Sorting Technics
#
def shell( arr ):
    n = len(arr)
    for i in [5,3,1]:
        dist = i
        for j in range(dist,n):
            temp = arr[j]
            z = j - dist
            while z >= 0 and arr[z] > temp:
                arr[z+dist] = arr[z]
                z -= dist
            arr[z+dist] = temp

def func():
    arr = [9,8,-7,6,-5,0,4,3,2,1]
    print(arr)
    shell(arr)
    print(arr)
func()
