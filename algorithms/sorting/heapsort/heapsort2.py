# Heap Sort Implementation in Python

class HeapSort:

      vec = []

      len = -1

      def __init__(self, arr):

           self.vec = arr

           self.len = len(arr)-1

           self.solve()

      def solve(self):

           self._createMinHeap()

           for i in range(self.len,1,-1):

               temp = self.vec[1]

               self.vec[1] = self.vec[i]

               self.vec[i] = temp

               self._minHeap(1,i-1)


      def _minHeap(self, node, n):

           val, base, ready = self.vec[ node ], 2 * node, 0

           while base <= n and ready == 0:
                    
                 if base < n and self.vec[ base ] > self.vec[ base + 1 ]:

                    base += 1
     
                 if val > self.vec[ base ]:

                    xor = self.vec[ node ] ^ self.vec[ base ]  

                    self.vec[ node ] = xor ^ self.vec[ node ]

                    self.vec[ base ] = xor ^ self.vec[ base ]

                    node = base
 
                    base *= 2
                    
                 else:

                    ready = 1
      

      def _createMinHeap(self):

          n = self.len

          for i in range(n/2, 0, -1):

              self._minHeap(i,n)

      def printLN(self):
           
          for i in range(1, self.len+1):
  
              print self.vec[i]            

      def toArray(self):

          out = []
 
          for i in range(1, self.len+1):
  
              out.append(self.vec[i])

          return out
 
ob = HeapSort([0,9,8,7,6,5,4,3,2,1,-1,22,222]) 

ob.printLN()

print ob.toArray()
