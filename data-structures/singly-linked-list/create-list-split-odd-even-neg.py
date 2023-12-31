class Node:
    def __init__(self):
        self.data = None
        self.next = None

def createlist(arr):
    head = None
    for i in arr:
        if head is None:
            head = Node()
            head.data = i
            head.next = None
        else:
            c = Node()
            c.data = i
            c.next = head
            head = c
    return head

def split_list(head):

    evenHead = Node()
    oddHead = Node()
    negHead = Node()

    evenLast = evenHead
    oddLast = oddHead
    negLast = negHead

    while head:
        if head.data % 2 == 1 and head.data > 0:
            oddLast.next = head
            oddLast = head
            head = head.next
            oddLast.next = None
        elif head.data % 2 == 0 and head.data > 0:
               evenLast.next = head
               evenLast = head
               head = head.next
               evenLast.next = None
        else:
            negLast.next = head
            negLast = head
            head = head.next
            negLast.next = None

    return evenHead.next, oddHead.next, negHead.next

def reverse(head):

    curr = head
    next2 = None
    prev = None

    while curr is not None:

        next2 = curr.next
        curr.next = prev
        prev = curr
        curr = next2;

    return prev

def display(head):

    while head:

        print(head.data, end = " ")
        head = head.next

    print()

def main():

    arr = [-100,1,2,-4,3,4,5,6,7,8,-1,-5,10]
    head = createlist(arr)
    head = reverse(head)
    display(head)
    even,odd,neg = split_list(head)
    display(odd)
    display(even)
    display(neg)

if __name__ == "__main__":
    main()
