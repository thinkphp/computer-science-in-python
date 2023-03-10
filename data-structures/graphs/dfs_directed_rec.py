def func():
    def dfs(node):
        print(node, end = " ")
        explored[node] = 1
        for i in range(nodes+1):
            if matrix[node][i] == 1 and explored[i] == 0:
                dfs(i)

    file = open("directed_graph.in","r")
    line = [int(i) for i in file.readline().split(" ")]
    nodes = int(line[0])
    edges = int(line[1])
    explored = [0] * (nodes+1)
    matrix = [[0 for column in range(nodes+1)] for row in range(nodes+1)]
    for k in range(0, edges):
       line = [int(i) for i in file.readline().split(" ")]
       x = int(line[0])
       y = int(line[1])
       matrix[x][y] = 1
    startNode = 1   
    dfs(startNode)

func()
