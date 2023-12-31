class Node:
    def __init__(self):
        self.data = None
        self.next = None

def CreateList(nr):
    head = None
    while nr:
        if head is None:
            head = Node()
            head.data = nr % 10
            head.next = None
        else:
            c = Node()
            c.data = nr % 10
            c.next = head
            head = c
        nr //= 10
    return head

def display(head):

    while head:
        print(head.data, end = "")
        head = head.next
    print()

def permut(head):
    q = head
    while q.next:
        q = q.next
    q.next = head
    head = head.next
    q.next.next = None
    return head

def main():
    nr = 1234567
    head = CreateList(nr)
    display(head)
    aux = head
    head = permut(head)
    display(head)
    while aux != head:
        head = permut(head)
        display(head)

if __name__ == "__main__":
    main()
