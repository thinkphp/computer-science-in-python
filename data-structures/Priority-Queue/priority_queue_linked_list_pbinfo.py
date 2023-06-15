class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):

        #initialize an empty head node
        self.head = None

    def empty(self):
        return self.head is None

    def length(self):
        pass

    def enqueue(self, data, priority):
        #create a new node with data and priority
        new_node = Node(data, priority)

        #check if the queue is empty or the new node has higher
        #priority than the header node
        if self.empty() or new_node.priority > self.head.priority:
           new_node.next = self.head
           self.head = new_node
        else:

           prev = self.head
           curr = self.head.next

           while curr is not None and new_node.priority <= curr.priority:
               prev = curr
               curr = curr.next

           new_node.next = curr
           prev.next = new_node

    def dequeue(self):

        #check if the queue is empty
        if self.empty():

           raise Exception("The queue is empty!")
        else:

            # get the data of the head node and hold it in a variable.
            data = self.head.data
            # set the head node to its next node
            self.head = self.head.next

            # return data
            return data

    def peek(self):
        # check if the queue is empty
        if self.empty():
        # raise an exception
           raise Exception("The queue is empty!")
        else:
           return self.head.data

    

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
        fout.write(str(pq.peek())+ " ")
        pq.dequeue()     
fn()            
