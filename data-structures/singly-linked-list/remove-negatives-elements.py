#
# Author's name: Adrian Statescu Dumitru
# Description  : Removes all negative numbers in a list using simply linked list.
# License      : MIT
#
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

def remove_negs(head):

    q = Node()
    q.next = head
    last = q

    while head is not None:

        if head.data < 0:
            tmp = head
            last.next = head.next
            head = head.next
            del tmp
        else:
            head = head.next
            last = last.next

    return q.next

def display(head):
    c = head
    if head is None:
        print("Empty List")
    while c:
        print(c.data, end = " ")
        c = c.next
    print()

def main():
    arr = [-1,-2,-3,4,-5,-6,-7]
    head = createlist(arr)
    display(head)
    head = remove_negs(head)
    display(head)

if __name__ == "__main__":
    main()
