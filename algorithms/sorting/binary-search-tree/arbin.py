#Binary Tree Search with Inorder for sorting

class Node:

      value = 0
      left = 0
      right = 0 

      def __init__(self, value):
          
          self.value = value


class BinaryTree:

      root = 0

      output = [] 

      def add(self,value):

          if self.root == 0:

             self.root = Node(value)

          else:

             current = self.root

             while 1:

                   if value < current.value:
 
                      if current.left == 0:
                         current.left = Node(value)
                         break
                      else:
                         current = current.left 

                   else:

                      if current.right == 0:
                         current.right = Node(value)
                         break
 
                      else:
                         current = current.right



      def travers(self):
 
          self.inorder(self.root)
 
      def inorder(self,node):

          if node.left:
             self.inorder(node.left)
 
          self.output.append(node.value)

          if node.right:
             self.inorder(node.right)

      def get(self):

          return self.output
        
                 

#Step 1: create an instance of class
ob = BinaryTree()

#Step 2: add elements in Binary Tree
ob.add(8)
ob.add(1)
ob.add(9)
ob.add(2)
ob.add(0)

#Step 3: travers the tree in inorder
ob.travers()

#Step 4: display the sorted array
print ob.get()