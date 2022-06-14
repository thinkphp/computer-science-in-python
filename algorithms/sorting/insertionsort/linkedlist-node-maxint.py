class Node:
 
    def __init__(self, data):
 
        self.data = data
        self.next = None
 
 
def sort(arr):
 
    head = None
 
    maxint = 500050
 
    head = Node(maxint)
 
    for i in arr:
 
        newNode = Node(i)
 
        if newNode.data < head.data:
            newNode.next = head
            head = newNode
 
        else:
 
            c = head
            c2 = c.next
 
            while newNode.data > c2.data:
                c = c.next
                c2 = c2.next
 
            c.next = newNode
            newNode.next = c2
 
    ptr = head
    out = []
    while ptr.data != maxint:
         out.append(ptr.data)
         ptr = ptr.next
    return out
 
def main():
 
    arr = [9,8,78,6,5,4,43,-1,0,100]
 
    print(arr)
 
    arr = sort(arr)
 
    print(arr)
 
 
main()
