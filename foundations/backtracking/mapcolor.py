def init():
    stack[level] = 1

def succ():
    if stack[level]<4:
        stack[level]+=1
        return True
    return False

def valid():
    for i in range(level):
        if stack[level] == stack[i] and matrix[i][level] == 1:
            return False
    return True

def sol():
    return level == nodes

def printf():
    for i in range(1,nodes+1):
        print(stack[i], end = " ")
    print()

def bk():
    global level
    level = 2

    while level > 0:
       h = True
       v = False
       while h is True and v is False:
             h = succ()
             if h is True:
                 v = valid()
       if h is True:
           if sol() is True:
               printf()
           else:
               level+=1
               init()
       else:
            level-=1


def displayGraph():
    for i in range(nodes):
        for j in range(nodes):
            print(matrix[i][j], end = " ")
        print()

def func():
    global stack,nodes, edges, matrix
    nodes = 5
    edges = 8
    data = [ [1,2],[1,4],[2,3],[2,5],[3,1],[3,5],[4,5] ]
    matrix = [[0 for i in range(nodes+1)] for j in range(nodes+1)]
    stack = [0] * (nodes+10)

    for edges in data:
        x, y = edges[0], edges[1]
        matrix[x][y] = 1
        matrix[y][x] = 1
    #displayGraph()
    stack[1] = 1
    bk()
func()
