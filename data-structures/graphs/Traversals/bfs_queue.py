class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def enqueue(self, data):

        new_node = Node(data)
        if self.size > 0:
            self.tail.prev = new_node
            new_node.next = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size+=1

    def dequeue(self):
        if self.head == None:
            return None
        result = self.head
        self.head = self.head.prev
        self.size-=1
        return result.data

    def peek(self):
        if self.head != None:
           return self.head.data

    def get_size(self):
        return self.size

#Breadth First Search
def bfs(matrix, nodes, startNode):

    q = Queue()

    explored = [0] * (nodes + 1)

    explored[ startNode ] = 1

    q.enqueue( startNode )

    while q.get_size() > 0:

        node = q.peek()
        
        print(node+1, end =" ")
        
        q.dequeue()

        k = 0

        while k < nodes:

            if matrix[node][k] == 1 and explored[k] == 0:

                explored[ k ] = 1

                q.enqueue( k )

            k+=1

    print(q.get_size())

def func():

    file = open("graph.in","r")

    nodes = int( file.readline() )

    matrix = [[int(num) for num in line.split(' ')] for line in file]

    startNode = 2

    bfs(matrix, nodes, startNode)

func()
