#
# HeapSort.py - Heap Sort Algorithm Sorting an array of randomly permuted of values.
# Website <http://thinkphp.ro>(MIT License).
# Email   <mergesortv@gmail.com>.
# Copyright (c) 2015, Adrian Statescu.
# 
 
class HeapSort:

      def __init__(self, arr):

          self.len = len( arr )

          self.Heap = ['x' for i in range(0, self.len + 1) ]

          self.sizeHeap = 0

          for i in range(0, self.len):

              self.insertHeap( arr[ i ] )

      def insertHeap(self, val):

           self.sizeHeap += 1

           self.Heap[ self.sizeHeap ] = val

           self.up( self.sizeHeap )

      def up(self, child):

          parrent = child / 2

          while (parrent > 0):
                 
                 if(self.Heap[ parrent ] > self.Heap[ child ]):

                    self._swap(parrent, child)

                    child = parrent

                    parrent = child / 2  
 
                 else:

                    break

      def down(self, parrent):

          while(2 * parrent <= self.sizeHeap):     

                child = 2 * parrent

                if (2 * parrent + 1 <= self.sizeHeap and self.Heap[ 2 * parrent + 1 ] < self.Heap[ 2 * parrent ]):

                   child += 1

                if(self.Heap[ parrent ] < self.Heap[ child ]):

                   break; 
   
                self._swap(parrent, child)

                parrent = child
                 
      def get(self):
   
          return self.Heap 

      def removeHeap(self):

          val = self.Heap[ 1 ]

          self.Heap[ 1 ] = self.Heap[ self.sizeHeap ]

          self.sizeHeap -= 1

          self.down( 1 ) 

          return val

      def sorted(self):

          for i in range(1, self.len + 1):

              print self.removeHeap( ),

      def _swap(self, i, j):

          x = self.Heap[ i ] ^ self.Heap[ j ]

          self.Heap[ i ] = x ^ self.Heap[ i ]

          self.Heap[ j ] = x ^ self.Heap[ j ]

ob = HeapSort([9,8,7,5,2,1,0,-1,11])

ob.sorted()