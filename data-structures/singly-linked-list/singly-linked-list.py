# Singly Linked List  Data Structure
#
# add
# removeNode
# display
# reverse
# insertAfterNode
# insertBeforeNode
# sorting by insertion
#
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
         else:
             c = Node(value)
             c.next = self.head
             self.head = c

     def insertAfterNode(self, key, value):

         ptr = self.head

         while ptr.data != key:
               ptr = ptr.next

         c = Node(value)

         c.next = ptr.next

         ptr.next = c

     def insertBeforeNode(self, key, value):

         #we have two cases: before HEAD, where becames head and before nodes

         if self.head.data == key:

             newNode = Node(value)
             newNode.next = self.head
             self.head = newNode
         else:
             ptr = self.head

             while ptr.next.data != key:
                   ptr = ptr.next

             c = Node(value)
             c.next = ptr.next
             ptr.next = c


     def removeNode(self, key):

         if self.head.data  == key:

            ptr = self.head
            self.head = self.head.next
            del ptr

         else:

             ptr = self.head

             while ptr.next.data != key:
                   ptr = ptr.next

             c = ptr.next
             ptr.next = c.next
             del c


     def display(self):

         c = self.head

         while c is not None:
             print(c.data, end = " ")
             c = c.next

     def reverse(self):
          curr = self.head
          next = None
          prev = None

          while curr is not None:
              next = curr.next
              curr.next = prev
              prev = curr
              curr = next

          self.head = prev

          print("\nReverse ->", end = " ")

          self.display()

     def sort(self, arr):

         MAXINT = 5000050

         self.head = Node(MAXINT)

         n = len(arr)

         for i in range(n):

             c = Node(arr[i])

             if c.data < self.head.data:
                 c.next = self.head
                 self.head = c

             # 1, 2, 3, 4, 23, MAXINT
             # 17
             else:
                  ptr1 = self.head
                  ptr2 = ptr1.next

                  while c.data > ptr2.data:
                       ptr1 = ptr1.next
                       ptr2 = ptr2.next
                  ptr1.next = c
                  c.next = ptr2


         ptr = self.head

         while ptr.data != MAXINT:
               print(ptr.data, end =" ")
               ptr = ptr.next


def main():
    
    value = int(input("value =  "))

    obj = LinkedList()

    while value != 0:

          obj.add(value)

          value = int(input("value =  "))

    obj.display()

    obj.reverse()

    key = int(input("del key = "))

    obj.removeNode(key)

    obj.display()

    key = int(input("insert after key = "))

    obj.insertAfterNode(key, 7777)

    obj.display()

    key = int(input("insert before key = "))

    obj.insertBeforeNode(key, 8888)

    obj.display()
    

    obj = LinkedList()
    
    arr = [200,9,8,7,-6,-5,11,101]
    
    print()
    
    obj.sort(arr)
main()
