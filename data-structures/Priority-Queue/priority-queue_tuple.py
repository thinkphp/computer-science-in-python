class PriorityQueue:

      def __init__(self):
          #create an empty list to store the queue
          self.queue = []
          self.data = None
          self.priority = None

      def enqueue(self, data ,priority):
          self.data = data
          self.priority = priority
          #append a new tuple with value and priority to the queue
          self.queue.append((data,priority))

      def dequeue(self):
          #check if the queue is empty
          if not self.queue:
              return
          #find the index of the tuple with the highest priority
          max_index = 0
          max_priority = self.queue[0][1]
          for i in range(1, len(self.queue)):
              if self.queue[i][1] > max_priority:
                  max_priority = self.queue[i][1]
                  max_index = i
          return self.queue.pop(max_index)

      def peek(self):
        max_index = 0
        max_priority = self.queue[0][1]
        for i in range(1, len(self.queue)):
            if self.queue[i][1] > max_priority:
                max_priority = self.queue[i][1]
                max_index = i
        return self.queue[max_index]
def fn():
    pq = PriorityQueue()
    N = 7
    K = 3
    Arr = [1, 23, 12, 9, 30, 2, 50]
    for i in Arr:
        pq.enqueue(i,i)
    while K:
        print(pq.peek()[0], end =" ")
        pq.dequeue()
        K-=1

fn()
