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

    def __str__(self):
        # initialize an output string variable
        output = ""
        #initialize a current node variable
        current = self.head
        #loop until the current node is None
        while current is not None:
            #append the data and priority of the current node
            #to the output string with with brackets and commas
            output += f"({current.data},{current.priority}),\n"
            #move the current node to the next node
            current = current.next
        output = output[:-2]
        return output
def fn():
    pq = PriorityQueue()
    pq.enqueue("react",101)
    pq.enqueue("angular",113)
    pq.enqueue("vue",17)
    pq.enqueue("ioi",232)
    print(pq)

    queue = PriorityQueue()
    arr = [3,4,5,6,11,3,44,145]
    
    for i in range(0, len(arr)):
        queue.enqueue(arr[i],arr[i])
        
    for i in range(0, len(arr)):
        print(queue.peek())
        queue.dequeue()
fn()
