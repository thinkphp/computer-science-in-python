#FIFO = First In First Out
#
# Methods:
# - enqueue(elem)
# - dequeue()
# - peek()
# - getSize()
#
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class Queue:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.tail = node
            self.head = node
            print("Enqueue: ", data, end = " ")
        else:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node
            print("Enqueue: ", data, end ="")
        self.size +=1
        print("| Size", self.size)

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

    def getSize(self):
        return self.size


    def dequeue(self):
        if self.head == None:
            print("Queue is empty!")
            return
        else:
            data = self.head.data
            self.head = self.head.prev
            self.size-=1
            print("Dequeue: ", end="")
            return data

def fn():
    q = Queue()
    for i in [1,2,3,4,5,6,7]:
        q.enqueue(i)

    print("size: ",q.getSize())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print("size: ",q.getSize())    
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("size: ",q.getSize())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
fn()
