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

          for i in range(self.len - 1, 0, -1):

              temp = self.vec[0]
              self.vec[0] = self.vec[i]
              self.vec[i] = temp
              
              self._minHeap(0, i-1)  

      def _minHeap(self, node, n):

           val = self.vec[ node ]
           base = 2 * node + 1
           ready = 0
            
           while base <=n and ready == 0:

                 if base < n and self.vec[ base + 1] < self.vec[ base ]:
                    base += 1
                 if val > self.vec[ base ]:

                    #swap the items of array
                    #node - first index of item
                    #base - second index of item
                    temp = self.vec[ base ]
                    self.vec[ base ] = self.vec[ node ]
                    self.vec[ node ] = temp

                    node = base
                    base = base * 2   

                 else:
                    ready = 1       


      def _createMinHeap(self):

          for i in range(self.len/2-1,-1,-1):

              self._minHeap(i, self.len)

      def printLN(self):
           
          for i in range(0, self.len+1):
  
              print self.vec[i]            

      def toArray(self):

          out = []
 
          for i in range(0, self.len+1):
  
              out.append(self.vec[i])

          return out
 
ob = HeapSort([3,2,1,0,-1,-2,-3]) 

print ob.toArray()
