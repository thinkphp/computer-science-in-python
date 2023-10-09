class Queue:
    def __init__(self, capacity):
        # a list to store the elements of the queue
        self.arr = []
        self.capacity = capacity

    def enqueue(self,data):
        if self.isFull() is True:
            print("The Queue is Full")
            return None
        print("Added to Queue: ", data)
        self.arr.append(data)

    def dequeue(self):
        if self.isEmpty() is True:
           print("The Queue is Empty!")
           return None
        data = self.arr[0]
        print("Remove from Queue: ", data)
        self.arr.pop(0)
        return data

    def display(self):
        if self.isEmpty() is True:
            print("Warning: the Queue is Empty. Nothing to display.")
            return None
        for elem in self.arr:
            print(elem, end = " ")
        print()

    def size(self):
        return len(self.arr)
    def isEmpty(self):
        #return True if the length of the array is zero
        return len(self.arr) == 0
    def isFull(self):
        return self.capacity == len(self.arr)
def main():
    q = Queue(100)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.display()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.display()
main()
