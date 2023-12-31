class Node:
    def __init__(self):
        self.data = 0
        self.next = None

#insertion sort using Linked List
def InsertSort( arr ):

    bigNum = 99999

    head = Node()
    head.data = bigNum
    head.next = None

    for num in arr:

        new_node = Node()
        new_node.data = num

        if num < head.data:
            new_node.next = head
            head = new_node
        else:
            c = head
            c1 = head.next
            while num > c1.data:
                c = c.next
                c1 = c1.next
            c.next = new_node
            new_node.next = c1

    while head and head.data != bigNum:

            print(head.data, end = " ")

            head = head.next

def LinkedList( arr ):

    head = None
    for i in arr:
        if head is None:
           head  = Node()
           head.data = i
           head.next = None
        else:
            c = Node()
            c.data = i
            c.next = head
            head = c
    return head

def display(head):

    while head:
        print(head.data, end = " ")
        head = head.next

def reverse( arr ):
    print()
    list = LinkedList( arr )
    display( list )

def main():
    arr = [9,4,5,-6,7,8,-1,-8,-101,1000,9001]
    print(arr)
    print("\nInsertion Sort: ", end ="\n")
    InsertSort(arr)
    print("\nReverse: ", end ="\n")
    reverse(arr)

if __name__ == "__main__":
    main()
