class Node(object):

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.size > 0:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size +=1
    def dequeue(self):
        if self.head == None:
            return None
        result = self.head
        self.head = self.head.prev
        self.size -=1
        return result.data
    def peek(self):
        if self.head:
           return self.head.data
        return None

    def get_size(self):
        return self.size

def func():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.peek())
func()
