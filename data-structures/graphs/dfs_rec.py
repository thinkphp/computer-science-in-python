def func():

    def dfs( node ):

        print("%d "% (node+1), end = "")

        explored[node] = 1

        for i in range(0, nodes):

            if matrix[node][i] == 1 and explored[i] == 0:

                dfs( i )



    file = open("graph.in","r")

    nodes = int(file.readline())

    matrix = [[int(num) for num in line.split(' ')] for line in file]

    explored = [0] * (nodes+1)

    startNode = 1

    dfs( startNode )

func()
