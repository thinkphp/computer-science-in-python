def fn():

    with open("spectacole.in","r") as file:

         matrix = [ [int(j) for j in line.split(" ")] for line in file]

    n = int(matrix.pop(0)[0])

    print("Number of spectacles = ",n)

    matrix = sorted(matrix, key = lambda x: x[1])
    
    print(matrix)

    count = 1

    curr = matrix[ 0 ][ 1 ]

    for i in range( 1, n ):

        if matrix[ i ][ 0 ] >= curr:

            curr = matrix[ i ][ 1 ]

            count +=1
            
    print("Count = ", count)
fn()
