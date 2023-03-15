
#Breadth First Search
def bfs(matrix, nodes, startNode):

    Queue = [0] * (nodes+1)
    explored = [0] * (nodes+1)
    first = 0
    last = 0
    explored[startNode] = 1
    Queue[0] = startNode

    while first<=last:

        node = Queue[first]

        k = 0

        while k < nodes:

            if matrix[node][k] == 1 and explored[k] == 0:

                explored[k] = 1
                last += 1
                Queue[last] = k

            k+=1

        first+=1
    for i in range(nodes):
         print(Queue[i]+1, end = " ")

def func():

    file = open("graph.in","r")

    nodes = int(file.readline())

    matrix = [[int(num) for num in line.split(' ')] for line in file]

    startNode = 2

    bfs(matrix, nodes, startNode)

func()
