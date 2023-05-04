#LIFO = Last In Last Out
# Methods:
#  - push(elem)
#  - pop()
#  - getTop()
#  - isEmpty()
#  - isFull()
#
class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.vec = [0] * (capacity + 2)
        self.top = -1

    def push(self, elem):
        if not self.isFull():
            self.top+=1
            self.vec[self.top] = elem
            print("Pushed: ", elem)
            print("Top: ", self.top)
        else:
            print("Stack Overflow!")
            return
    def pop(self):
        if self.isEmpty():
            print("Empty Stack!")
            return
        else:
            data = self.vec[self.top]
            self.top -=1
            return data

    def isFull(self):
        return self.capacity == self.top - 1

    def isEmpty(self):
        return self.top == -1

    def getTop(self):
        return self.vec[self.top]

def fn():
    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(71)
    stack.push(71)
    print(stack.pop())
    print(stack.getTop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    st = Stack(100)
    str = "123456789"
    for i in str:
        st.push(i)
    for i in str:
        print(st.pop(), end="")

fn()
