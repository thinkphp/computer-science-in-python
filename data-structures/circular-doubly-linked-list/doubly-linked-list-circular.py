"""
#description:
# CircularDoublyLinkedList
# License: MIT
# Date: 10 Nov

class CircularDoublyLinkedList

Data members:
  self.head = None

Methods:
1 - add_front(data)
2 - add_back(data)
3 - display()
4 - add_after(position, data)
5 - add_before_element(target_node, data)
6 - add_after_element(target_node, data)
7 - remove( data )
8 - modify( old_data, new_data )
9 - get_size()
10 - is_empty()
11 - Clear()
12 - Contains(data)
13 - get_first()
14 - get_last()
15 - remove_first()
16 - find_position(node_value)

"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:

      def __init__(self):
        self.head = None
        self.size = 0 #track list size

      def add_front(self, data):
          new_node = Node( data )

          if self.head is None:
              new_node.next = new_node
              new_node.prev = new_node
              self.head = new_node
              self.size+=1
          else:
              last = self.head.prev

              new_node.next = self.head
              new_node.prev = last

              last.next = new_node
              self.head.prev = new_node

              self.head = new_node
              self.size+=1

      def get_size(self):
              """this function Returns the number of elements in the list """
              return self.size

      def is_empty(self):
          """check if the list is empty """
          return self.head is None

      def clear(self):
            self.head = None
            self.size = 0

      def add_back(self, data):

            new_node = Node( data )

            if self.head is None:
                new_node.next = new_node
                new_node.prev = new_node
                self.head = new_node
                self.size+=1
            else:
                last = self.head.prev

                new_node.next = self.head
                new_node.prev = last

                last.next = new_node
                self.head.prev = new_node
                self.size+=1

      def add_after(self, position_specified, data):

          if self.head is None:
               return

          current = self.head

          for _ in range( position_specified):
              current = current.next
              if current == self.head:
                 return #am ajuns la inceput

          new_node = Node( data )

          new_node.next = current.next
          new_node.prev = current

          current.next.prev = new_node
          current.next = new_node

      def modify(self, old_value, new_value):

          if self.head is None:
              return

          current = self.head

          while True:

              if current.data == old_value:
                  current.data = new_value
                  return

              current = current.next
              if current == self.head:
                  print("Nu se afla in lista")
                  break

      def remove(self, data):

          if self.head is None:
              return

          current = self.head#atribuire self.head to current node

          while True:
             if current.data == data:
                 print(f"Nodul {data} A fost sters cu success")
                 if current.next == current:
                    self.head = None
                 else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    if current == self.head:
                        self.head = current.next
                 return

             current = current.next

             if current == self.head:
                 print(f"Elementul {data} nu se afla in lista dublu inlantuita circulara")
                 break


      def add_before_element(self, target_value, data):

          if self.head is None:
              return

          current = self.head

          while True:
              if current.data == target_value:

                  new_node = Node( data )

                  new_node.next = current

                  new_node.prev = current.prev

                  current.prev.next = new_node

                  if current == self.head:
                      self.head = new_node
                  return

              current = current.next

              if current == self.head:
                  break #target value not found

      def add_after_element(self, target_value, data):

          if self.head is None:
              return

          current = self.head

          while True:

              if current.data == target_value:

                  # se creeaza nodul
                  new_node = Node( data )

                  # update links
                  new_node.next = current.next
                  new_node.prev = current
                  current.next.prev = new_node
                  current.next = new_node
                  return

              current = current.next
              if current == self.head:
                  break #not found

      def contains(self, data):

          """Check if a value exists in the list or not"""

          if self.head is None:
              return False

          current = self.head

          while True:

              if current.data == data:
                  return True
              current = current.next
              if current == self.head:
                 break

          return False


      def display(self):
           if self.head is None:
               print("Lista este goala")
               return
           current = self.head

           while True:
               print(current.data, end = " ")
               current = current.next
               if current == self.head:
                  break
           print()

def main():
    list = CircularDoublyLinkedList()

    list.add_back(1)
    list.add_back(2)
    list.add_back(3)
    list.add_back(4)
    list.add_back(5)

    list.display()
    print(f"Numarul de elemente din lista {list.get_size()}")


    list.modify(1, 55)
    list.display()

    list.add_after(1, 89)
    list.display()

    list.remove(2)
    list.display()

    list.add_before_element(4,1001)
    list.display()

    list.add_after_element(4,1002)
    list.display()

    check_value = int(input("Dati un nod de cautare:"))

    if list.contains(check_value) is True:

        print(f"Nodul {check_value} se afla in lista dublu inlantuita circulara.")
    else:

        print(f"Nodul {check_value} NU se afla in lista dublu inlantuita circulara.")
main()
