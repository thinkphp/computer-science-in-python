#
# BinarySearchTree__Sort.py - Binary Search Tree Sort or Tree Sort Algorithm Sorting an array of randomly permuted of values.
# Big O Notation
# 1.Worst-case performance     -> O(n^2)     if unbalanced
#                              -> O(n log n) if balanced
# 2.Best-case performance      -> O(n log n)         
# 3.Average-case performance   -> O(n log n)         
# Website <http://adrianstatescu.ro>(MIT License).
# Email   <mergesortv@gmail.com>.
# Copyright (c) 2015, Adrian Statescu.
# 
 
class Node:
      
      def __init__( self, val ):

          self.left = 0

          self.right = 0

          self.info = val      

class TreeSort:

      def __init__( self ):

          self.root = 0

          self.L = []

      def add(self, val):

          if self.root == 0:

             self.root = Node( val )   

          else:

            self.curr = self.root

            while 1:

                  if val < self.curr.info:

                     if self.curr.left == 0:

                        self.curr.left = Node( val )

                        break

                     else:

                        self.curr = self.curr.left

                  else:

                     if self.curr.right == 0:

                        self.curr.right = Node( val )

                        break       

                     else:

                        self.curr = self.curr.right

      def travers( self ):

              self._inorder( self.root )
          
      def _inorder( self, node ):

              if node.left:

                 self._inorder( node.left )

              self.L.append ( node.info )

              if node.right:

                 self._inorder( node.right )

      def getList( self, node ):

              L = []

              if node.left:

                 L.extend( self.getList( node.left ) )

              L.append( node.info )

              if node.right:

                 L.extend( self.getList( node.left ) )

              return L

      def getSorted( self ):

              return self.L