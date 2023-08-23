def display(matrix, countries):

    for i in range(countries):

        for j in range(countries):

            print(matrix[i][j], end = " ")
        print()

def solve(matrix, countries):

    colors = [0] * countries

    for i in range(1, countries):

        col = -1
        
        ok = False

        while ok is not True:

            col += 1

            ok = True

            for k in range( i ):

                if matrix[k][i] == 1 and colors[k] == col:

                    ok = False

        colors[i] = col

    final_list = list(map(lambda x: x+1, colors))

    print(final_list)

def fn():

    filename = "graphcoloring.in"

    with open(filename, 'r') as f:

         matrix = [[int(num) for num in line.split(' ')] for line in f]

    countries = int(matrix.pop(0)[0])

    display(matrix, countries)

    solve(matrix, countries)

fn()
