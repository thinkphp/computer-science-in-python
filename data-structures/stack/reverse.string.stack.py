class Stack:
     def __init__(self, c):
        self.top = -1
        self.capacity = c
        self.arr = [0] * (c + 1)

def createStack(capacity):
    stack = Stack(capacity)
    return stack

def isEmpty(stack):
    return stack.top == -1

def isFull(stack):
    return stack.capacity == stack.top - 1

def push(stack, elem):
    if isFull(stack) is True:
        return
    else:
      stack.top += 1
      stack.arr[stack.top] = elem

def pop(stack):
    if not isEmpty(stack):
       x = stack.arr[stack.top]
       stack.top -=1
       return x
    return 0

def reverse(str, n):
    stack = createStack(n)
    for i in str:
        push(stack, i)
    for i in str:
        print(pop(stack), end = "")

def func():
    str = "MayAnnCampaneraVergara"
    n = len(str)
    reverse(str, n)
func()
