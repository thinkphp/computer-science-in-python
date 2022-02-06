def main():

    arr = [9,8,7,6,5,4,3,2,1,0]

    n = len( arr )  

    print( arr )

    for i in range(0, n - 1):

        indMin = i

        for j in range(i + 1, n):

            if arr[ j ] < arr[ indMin ]:

               indMin = j

        arr[ indMin ] = arr[ indMin ] + arr[ i ]

        arr[ i ] = arr[ indMin ] - arr[ i ]

        arr[ indMin ] = arr[ indMin ] - arr[ i ]

    print("sorted array")
    print(arr)    

main()    
