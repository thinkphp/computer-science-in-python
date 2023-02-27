def init(level):
    stack[level] = 0

def succ(level):

    if stack[level]<nodes:
        stack[level]+=1
        return True
    else:
        return False

def valid(level):

    if  matrix[stack[level-1]][stack[level]] == 0:
        return False
    else:
        for i in range(1, level):
            if stack[level] == stack[i]:
                return False
    return True

def sol(level):
    return level == nodes and matrix[startNode][stack[level]] == 1

def printf():
    for i in range(1, nodes+1):
        print(stack[i], end = " ")
    print()

def back(level):
    init(level)
    while succ(level):
        if valid(level):
            if sol(level):
                printf()
            else:
                back(level+1)

def displayGraph():
    for i in range(1, nodes+1):
        for j in range(1,nodes+1):
            print(matrix[i][j], end = " ")
        print("")
def func():
    global stack,nodes, edges, matrix, startNode
    nodes = 6
    edges = 10
    data = [ [1,2],[1,6],[2,3],[2,5],[3,4],[3,5],[3,6],[4,5],[5,6],[6,1] ]
    matrix = [[0 for i in range(nodes+1)] for j in range(nodes+1)]
    stack = [0] * (nodes+1)

    for edge in data:
        x,y = edge[0], edge[1]
        matrix[x][y] = 1
        matrix[y][x] = 1

    #displayGraph()

    startNode = 3

    stack[1] = startNode

    back(2)

func()
