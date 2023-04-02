class Stack:
  
  def __init__(self, capacity):  
     self.capacity = capacity
     self.top = -1
     self.arr = [0] * (capacity + 1)

  def isFull(self):
      return self.capacity == self.top + 1
    
  def isEmpty(self):
      return self.top == -1

  def push(self,data) -> None:
    if not self.isFull():
       self.top += 1
       self.arr[self.top] = data
    else:
       print("The Stack is Full")

  def pop(self):
    if not self.isEmpty():
       self.top -=1       

  def get_top(self):    
    return self.arr[self.top]
    
def fn():
    str = "12345"
    print(str)
    n = len(str)
    stack = Stack(n+1)
    for i in str:
        stack.push(i)
    for i in range(0,n):
        print(stack.get_top(), end ="")
        stack.pop()
    print()  
fn()  
