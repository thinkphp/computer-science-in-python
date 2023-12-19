class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

      def __init__(self):

          self.head = None

      # insert at the end
      def insert2(self, value):

          newNode = Node(value)

          if self.head is None:
              self.head = newNode
          else:
              curr = self.head
              while curr.next is not None:
                  curr = curr.next
              curr.next = newNode

      # insert at beginning
      def insert(self, value):

          newNode = Node(value)

          if self.head is None:
              self.head = newNode
          else:
              newNode.next = self.head
              self.head = newNode

      # display the nodes
      def traversal(self):

          c = self.head

          try:
              if c is None:
                  raise Exception("Head is NULL")
          except Exception as e:
              print(str(e))

          while c is not None:

              print(c.data, end = " ")
              c = c.next
          print()

      def del_from_begin(self):

           try:
               if self.head is None:
                   raise Exception("Empty Linked List")
               else:
                   temp = self.head
                   self.head = self.head.next
                   del temp
           except Exception as e:
               print(str(e))

      def del_from_end(self):

              try:
                  prev = None

                  curr = self.head

                  if curr is None:
                     raise Exception("The head of the Linked List is null")

                  while curr.next is not None:

                     prev = curr

                     curr = curr.next

                  prev.next = curr.next

                  del curr

              except Exception as e:
                   print(str(e))

def main():
    obj = LinkedList()
    obj.insert2(187)
    obj.insert2(75)
    obj.insert2(22)
    obj.insert2(13)
    obj.insert2(87)
    print("Linked List:")
    obj.traversal()
    obj.del_from_begin()
    obj.traversal()
    obj.del_from_end()
    obj.traversal()
main()
