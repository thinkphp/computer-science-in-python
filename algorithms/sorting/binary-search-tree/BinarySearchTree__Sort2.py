#
# BinarySearchTree__Sort.py - Merge Sort Algorithm Sorting an array of randomly permuted of values.
# Website <http://adrianstatescu.ro>(MIT License).
# Email   <mergesortv@gmail.com>.
# Copyright (c) 2015, Adrian Statescu.
# 
 
class Node:
      
      def __init__( self, val ):

          self.left = None

          self.right = None

          self.info = val      

class TreeSort:

      def __init__( self ):

          self.root = None

      def add(self, val):

          if self.root is None:

             self.root = Node( val )   

          else:

            self.curr = self.root

            while 1:

                  if val < self.curr.info:

                     if self.curr.left is None:

                        self.curr.left = Node( val )

                        break

                     else:

                        self.curr = self.curr.left

                  else:

                     if self.curr.right is None:

                        self.curr.right = Node( val )

                        break       

                     else:

                        self.curr = self.curr.right

      def travers( self ):

              self._inorder( self.root )
          
      def _inorder( self, node ):

              if not node.left is None:

                 self._inorder( node.left )

              print node.info,

              if not node.right is None:

                 self._inorder( node.right ) 


ob = TreeSort()
ob.add(5)
ob.add(4)
ob.add(3)
ob.add(2)
ob.add(1)
ob.travers()