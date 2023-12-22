# Definition for singly-linked list.
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

def CreateList():
    head = None
    n = int(input("n="))
    for _ in range(n):
        node_value = int(input("node value = "))
        new_node = Node(node_value)
        new_node.next = head
        head = new_node
    return head

def addition(list1, list2):

    dummyHead = Node(0)
    p, q = list1, list2
    curr = dummyHead
    carry = 0

    while p or q:
      x = p.data if p else 0
      y = q.data if q else 0

      summa = x + y + carry

      curr.next = Node(summa%10)

      carry = summa // 10

      if p:
          p = p.next
      if q:
          q = q.next

      curr = curr.next

    if carry > 0:

        curr.next = Node(carry)

    return dummyHead.next

def reverse(head):

    curr = head
    next2 = None
    prev2 = None

    while curr is not None:

        next2 = curr.next
        curr.next = prev2
        prev2 = curr
        curr = next2

    return prev2

def DisplayList(head, reverse_display = False):

    if reverse_display:
        head = reverse( head )

    while head:
        print(head.data, end = " ")
        head = head.next;

class main():
    list1 = CreateList();
    list2 = CreateList();
    answer = addition(list1, list2)
    print("Number 1:")
    DisplayList(list1, reverse_display = True)
    print()
    print("Number 2:")
    DisplayList(list2, reverse_display = True)
    print("\nSum = number1 + number2", end = "\n")
    DisplayList(answer, reverse_display = True)
if __name__ == '__main__':
    main()
