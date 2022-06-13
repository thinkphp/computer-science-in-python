class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None

    def add(self, value):

        if self.head is None:
           self.head = Node(value)
           self.next = None
        else:
            c = Node(value)
            c.next = self.head
            self.head = c
    def remove(self, key):
        if self.head.data == key:
            ptr = self.head
            self.head = self.head.next
            del ptr
        else:
            c = self.head
            while c.next.data != key:
                c = c.next
            ptr = c.next
            c.next = ptr.next
            del ptr


    def display(self):
          c = self.head
          while c is not None:
              print(c.data, end =" ")
              c = c.next
    def reverse(self):
           curr = self.head
           prev = None
           next = None

           while curr is not None:
               next = curr.next
               curr.next = prev
               prev = curr
               curr = next

           self.head = prev
           self.display()
def main():
    obj = LinkedList()

    value = int(input("value = "))
    while value != 0:
          obj.add(value)
          value = int(input("value = "))
    obj.display()
    print()
    key = int(input("Key to remove = "))
    obj.remove(key)
    obj.display()
    print()
    print("Reverse: ")
    obj.reverse()
main()
