class PriorityQueue:

      def __init__(self):
          
          self.queue = []
          self.data = None
          self.priority = None

      def enqueue(self, data ,priority):
          self.data = data
          self.priority = priority          
          self.queue.append((data,priority))

      def dequeue(self):
          
          if not self.queue:
              return          
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
    fout = open("sortare.out","w")    
    with open("sortare.in","r") as file:
         data = file.readlines() 
    n = int(data[0])
    arr = data[1] 
    arr = list(map(int, arr.split()))    
             
    pq = PriorityQueue()
             
    for i in range(n):
        pq.enqueue(arr[i], arr[i])         
             
    for i in arr:
        fout.write(str(pq.peek()[0])+ " ")
        pq.dequeue()     
fn()            
