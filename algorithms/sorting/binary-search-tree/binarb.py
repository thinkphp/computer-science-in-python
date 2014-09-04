# Binary Tree Search

class BinaryTreeSearch:

      root = 0

      def __init__(self):

          self.root = 0          

      def travers(self):

          self._inorder(self.root)

      def _inorder(self, node):

          if node[1] != 0:
             self._inorder(node[1])
          
          print node[0]

          if node[2] != 0:
             self._inorder(node[2])  

      def add(self,value): 

          Node = [value,0,0]

          if self.root == 0:

             self.root = Node

          else:

             current = self.root

             while 1:

               if value < current[0]:

                 if current[1] == 0:

                   current[1] = Node
                   break

                 else:

                   current = current[1]   

               else:
                
                 if current[2] == 0:

                   current[2] = Node
                   break 

                 else:

                   current = current[2]   
                

ob = BinaryTreeSearch()

ob.add(8)     
ob.add(3)
ob.add(5)
ob.add(1)
ob.add(2)

print ob.root

ob.travers()
 
   

 

