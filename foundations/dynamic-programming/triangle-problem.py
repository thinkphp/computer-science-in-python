def fn():

    n = int(input())

    Tri = [[0 for _ in range(n+1)] for _ in range(n+1)]

    c = [[0 for _ in range(n+1)] for _ in range(n+1)]

    road = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):

        for j in range(1,i+1):

            Tri[i][j] = int(input())

    for i in range(1,n+1):

        for j in range(1,i+1):

            print(Tri[i][j], end = " ")

        print()

    for j in range(1,n+1):
        c[n][j] = Tri[n][j]

    for i in range(n - 1, 0, -1):

        for j in range(1, i + 1):

            if c[ i + 1 ][ j ] > c[ i + 1 ][ j + 1 ]:

               c[ i ][ j ] = Tri[ i ][ j ] + c[ i + 1 ][ j ]
                
               road[ i ][ j ] = j

            else:

               c[ i ][ j ] = Tri[ i ][ j ] + c[ i + 1 ][ j + 1 ]
               
               road[ i ][ j ] = j + 1

    print(c[1][1])

    i = j = 1

    while i <= n:

        print( Tri[ i ][ j ], end = " " )

        j = road[ i ][ j ]

        i += 1
fn()
