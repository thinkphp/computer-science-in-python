def func():
    
    def dfs(vertex):
        
        stack = [0] * (nodes+1)
        explored = [0] * (nodes+1)
        ptr = 0
        stack[ptr] = vertex
        explored[ vertex ] = 1
        print(vertex, end=" ")

        while ptr >= 0:
            node = stack[ptr]
            found = 0
            k = 1
            while not found and k < nodes+1:
                if matrix[node][k] == 1 and explored[k] == 0:
                    found = 1
                k += 1
            if not found:
                ptr -= 1
            else:
                print(k-1, end = " ")
                ptr += 1
                stack[ptr] = k-1
                explored[k-1] = 1

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
    dfs(startNode)
func()
