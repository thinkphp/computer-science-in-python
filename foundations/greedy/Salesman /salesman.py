def Greedy(nodes, matrix):
 
    BIG = 99999
    cost = 0
    node = 0
    start = node
    explored = [ 0 ] * (nodes+1)
    explored[node] = 1
 
    print(node+1, end = " ")
 
    for i in range(1, nodes):
 
        min = BIG
 
        for vertice in range(0, nodes):
 
            if matrix[node][vertice] != 0 and explored[vertice] == 0 and matrix[node][vertice] < min:
 
                min = matrix[node][vertice]
 
                next = vertice
 
        explored[next] = 1
 
        print(next+1, end = " ")
 
        cost = cost + matrix[node][next]
 
        node = next
 
    cost = cost + matrix[start][node]
 
    print(start+1, end = " ")
 
    print("\nCost =", cost)
 
def readMatrix():
    matrix = [[5],[0,1,5,5,3],[1,0,2,4,1],[5,2,0,6,1],[5,4,6,0,9],[3,1,1,9,0]]
    nodes = int(matrix.pop(0)[0])
    for i in range(nodes):
        for j in range(nodes):
            print(matrix[i][j], end =" ")
        print()
    print()
    return nodes, matrix
 
def readMatrixStd():
    nodes = int(input("nodes="))
    matrix = [[0 for j in range(nodes+1)] for i in range(nodes+1)]
    for i in range(0, nodes):
        for j in range(0, nodes):
            matrix[i][j] = int(input("matrix[%d][%d]="%(i,j)))
 
    for i in range(nodes):
        for j in range(nodes):
            print(matrix[i][j], end =" ")
        print()
 
    print()
 
    return nodes, matrix
 
def ReadFileMatrixAdjacency(filename):
 
    with open(filename, "r") as file:
        matrix = [ [int(j) for j in line.split(" ")] for line in file]
 
    nodes = int(matrix.pop(0)[0])
    for i in range(nodes):
        for j in range(nodes):
            print(matrix[i][j], end =" ")
        print()
    print()
    return nodes, matrix
 
def fn():
    filename = "salesman.in"
    #data = ReadFileMatrixAdjacency( filename )
    #data = readMatrix()
    data = readMatrixStd()
    nodes = data[0]
    matrix = data[1]
    Greedy(nodes, matrix)
fn()
