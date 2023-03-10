def func():

    def bfs(node):
        Q = [ 0 ] * ( nodes + 1 )
        first = 0
        last = 0
        explored = [0] * (nodes+1)
        Q[first] = node
        explored[node] = 1

        while first <= last:
            vertex = Q[first]
            k = 0
            while k < nodes+1:
                if matrix[vertex][k] == 1 and explored[k] == 0:
                  explored[k] = 1
                  last+=1
                  Q[last] = k
                k+=1
            first+=1

        for i in range(0, nodes):
            print(Q[i], end=" ")

    file = open("directed_graph.in","r")
    line = [int(i) for i in file.readline().split(" ")]
    nodes = int(line[0])
    edges = int(line[1])
    matrix = [[0 for column in range(nodes+1)] for row in range(nodes+1)]
    for k in range(0, edges):
       line = [int(i) for i in file.readline().split(" ")]
       x = int(line[0])
       y = int(line[1])
       matrix[x][y] = 1

    # start Node DFS
    startNode = 1
    bfs(startNode)
func()
