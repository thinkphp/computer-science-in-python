class Node:

    def __init__( self ):

        self.data = None
        self.next = None

def reverse(list):
    curr = list
    next2 = None
    prev2 = None

    while curr is not None:
        next2 = curr.next
        curr.next = prev2
        prev2 = curr
        curr = next2

    return prev2


def createlist():

    head = None

    str = input("Big Number = ")

    for digit in str:
        q = Node()
        q.data = int(digit)
        q.next = head
        head = q

    return head

def addition(list1,list2):
    head = Node()
    curr = head
    p = list1
    q = list2
    carry = 0

    while p or q:

        if p:
            x = p.data
        else:
            x = 0
        if q:
            y = q.data
        else:
            y = 0

        summa = x + y + carry

        carry = summa // 10

        curr.next = Node()
        curr.next.data = summa % 10

        if p:
            p = p.next
        if q:
            q = q.next

        curr = curr.next
    if carry > 0:
        curr.next = Node()
        curr.next.data = carry


    return head.next


def display(head):
    while head:
        print(head.data, end = "")
        head = head.next
    print()
def main():

    list1 = createlist()
    list2 = createlist()
    summa = addition(list1,list2)
    print("Suma = ", end = "")
    display(reverse(summa))


if __name__ == "__main__":
    main()
