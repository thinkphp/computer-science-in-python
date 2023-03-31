def setPartitions():
    def solve(level):
        if level == n+1:
            print(stack)
        else:
            for i in range(1,n+1):
                stack[level] = i
                if stack[level] <= stack[level-1]+1:
                    solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)
setPartitions()

def fulfilled():
    def solve(level):
        global sum
        if sum == n:
           for i in range(1, level):
               print(stack[i], end =" ")
           print()
        else:
           stack[ level ] = 0
           while stack[level]+sum < n:
               stack[level] += 1
               sum += stack[level]
               solve(level+1)
               sum -= stack[level]
    n = 3
    global sum
    stack = [0] * (n+1)
    sum = 0
    solve(1)
fulfilled()

def subsets():
    def solution(level):
        for i in range(1, level+1):
            print(stack[i], end = " ")
        print()
    def solve(level):
        if level <= n:
           for i in range(stack[level-1]+1, n+1):
               stack[level] = i
               solution(level)
               solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)
subsets()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size():
        return self.size

    def enqueue(self, data):
        node = Node(data)
        if self.size > 0:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size+=1

    def dequeue(self):
       if self.head:
        result = self.head
        print("dequeue %s" % self.head.data)
        self.head = self.head.prev
        self.size-=1
        return result.data
       return None

    def peek(self):
        if self.head == None:
           return None
        return self.head.data

q = Queue()
q.enqueue("x")
q.enqueue("b")
q.enqueue("c")
q.enqueue("1")
q.enqueue("2")
q.dequeue()
q.dequeue()
print(q.peek())
