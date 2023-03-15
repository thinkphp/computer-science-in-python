def RoyFloyd():

    def display():

        print("Matrix after Roy-Warshall")

        for i in range(1, nodes+1):

            for j in range(1, nodes+1):

                print(matrix[i][j], end = " ")

            print()

    def buildPath(i, j):

        k = 1

        found = False

        while k <= nodes and not found:

            if i != k and j != k and matrix[i][j] == matrix[i][k] + matrix[k][j]:

                print(k, end = " ")

                found = True

                buildPath(i, k)

                buildPath(k, j)

            k +=1

    def road(startpoint, endpoint):
        if matrix[startpoint][endpoint] < INF:
           print("Shorted Path from %d to %d has the length %d"% (startpoint, endpoint, matrix[startpoint][endpoint]))
           print(startpoint, end = " ")
           buildPath(startpoint, endpoint)
           print(endpoint)
        else:
            print("No Found.")

    def RoyWarshall():
        for k in range(1, nodes+1):
            for i in range(1, nodes+1):
                for j in range(1, nodes+1):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

    file = open("floyd.in", "r")
    line = file.readline().split(" ")
    nodes, edges = int(line[0]), int(line[1])
    matrix = [[0 for col in range(0, nodes+1)] for row in range(0, nodes+1)]

    INF = 1.e20

    for i in range(1, nodes+1):

        for j in range(1, nodes+1):

            if i == j:

                matrix[i][j] = 0

            else:

                matrix[i][j] = INF

    for i in range(1, edges+1):

        line = [int(i) for i in file.readline().split(" ")]

        x = line[0]

        y = line[1]

        c = line[2]

        matrix[x][y] = c

    RoyWarshall()

    startpoint = 1

    endpoint = 4

    road(startpoint,endpoint)

RoyFloyd()
