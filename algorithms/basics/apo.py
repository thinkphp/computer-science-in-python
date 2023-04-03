def perm():
    def accepted(level):
        for i in range(1, level):
            if stack[level] == stack[i]:
                return False
        return True
    def solve(level):
        if level == n + 1:
            for i in range(1,n+1):
                print(stack[i], end = " ")
            print()
        else:
            for i in range(1, n + 1):
                stack[level] = i
                if accepted(level):
                    solve(level+1)
    n = 3
    stack = [0] * (n+1)
    solve(1)

def fib(n):
    a = 0
    b = 1
    sol = []
    sol.append(a)
    sol.append(b)
    while n :
        r = a + b
        sol.append(r)
        a = b
        b = r
        n -= 1
    return sol

def euclid(a,b):

    while b:
        r = a % b
        a = b
        b = r

    return a

def gcd(a,b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def fn():
    def printf(level):
        for i in range(1, level+1):
            print(stack[i], end=" ")
        print()

    def subsets(level):
        if level <= n:
            for i in range(stack[level-1]+1,n+1):
                stack[level] = i
                printf(level)
                subsets(level+1)
    n = 3
    stack = [0] * (n+1)
    subsets(1)
fn()
print(euclid(10,3) == gcd(10,3))
print(fib(26))
perm()

class Stack:
    def __init__(self,c):
        self.capacity = c
        self.arr = [0] * (c + 1)
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.capacity == self.top - 1

    def push(self,data):
        if not self.isFull():
            self.top += 1
            self.arr[self.top] = data

    def pop(self):
        if not self.isEmpty():
            x = self.arr[self.top]
            self.top-=1
            return x

    def getTop(self):
        return self.arr[self.top]

class Node(object):
    def __init__(self,info):
        self.data = info
        self.next = None
        self.prev = None

class Queue(object):
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0;

    def enqueue(self,data):

        new_node = Node(data)
        if self.size > 0:
            self.tail.prev = new_node
            new_node.next = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size +=1

    def dequeue(self):
        if self.head == None:
            return None
        else:
            result = self.head
            self.head = self.head.prev
            self.size -=1
            return result.data
    def peek(self):
        if self.head != None:
            return self.head.data

    def get_size(self):
        return self.size

def FnQueue():
    q = Queue()
    q.enqueue(2)
    q.enqueue(23)
    q.enqueue(19)
    q.enqueue(32)
    print(q.peek())
    print(q.get_size())
    print(q.dequeue())
    print(q.get_size())
FnQueue()

def FnStack():
    str = "54321"
    print(str)
    stack = Stack(len(str))
    for i in str:
        stack.push(i)
    for i in str:
        print(stack.getTop(), end = "")
        stack.pop()
FnStack()
