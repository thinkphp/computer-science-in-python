class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = [0] * (capacity+2)
    def push(self, elem):
        if self.isFull() is True:
            print("Stack Overflow!")
            return
        else:
            self.top+=1
            self.stack[self.top] = elem
            print("Pushed to Stack:", elem)

    def pop(self):
        if self.isEmpty():
            print("Stack Empty!")
            return
        else:
            top = self.stack[self.top]
            self.top-=1
            return top

    def getTop(self):
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.capacity == self.top - 1

def fn():
    s = Stack(3)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    for i in [1,2,3]:
        print(s.pop(),end="")
fn()
