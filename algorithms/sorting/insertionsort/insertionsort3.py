def insertsort( arr ):

    n = len( arr )

    for i in range(1, n):

        temp = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > temp:

              arr[j+1] = arr[j]

              j -= 1

        arr[j+1] = temp      


def main():

    arr = [9,8,7,6,5]

    print(arr)

    insertsort(arr)

    print(arr)

main()
