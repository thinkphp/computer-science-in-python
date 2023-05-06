class Node:

    def __init__(self, info):
        self.data = info
        self.next = None
        self.prev = None

class Queue:

    def __init__(self):
        self.tail = None
        self.head = Node
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.tail = node
            self.head = node
        else:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node
        self.size+=1

    def dequeue(self):

        if self.head != None:
            data = self.head.data
            self.head = self.head.prev
            self.size-=1
        else:
            print("Queue is empty!")
            return

    def peek(self):

        return self.head.data

    def getSize(self):
        return self.size

def fn():
    q = Queue()
    for i in "MayAnnCampanera":
        q.enqueue(i)

    str1 = ""
    cnt = 0
    print(q.getSize())
    for i in "MayAnnCampanera":
        cnt+=1
        str1 += "<h"+str(cnt)+">"+q.peek()+"</h"+str(cnt)+"></br>"
        q.dequeue()
    print(q.getSize())
    q.dequeue()
    q.dequeue()
    print(str1)

fn()
