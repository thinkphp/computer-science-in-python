#class QuickSort
class QuickSort:
  
      #initial array to sort
      vec = []

      #number of elements 
      n = -1 
    
      #constructor of class QuickSort
      def __init__(self, arr):

           #assign the desired vector to sort
           self.vec = arr

           #compute the number of elements
           n = len( arr )

           #quick sort in action
           self._quicksort(0, n - 1)

      #QuickSort for the Win with XOR and middle pivot
      def _quicksort(self, li, ls):
 
          i = li
          j = ls
          x = -1
          p = self.vec[(li+ls)>>1]

          while i <= j:
          
             while self.vec[i] < p:
                   i += 1

             while self.vec[j] > p:
                   j -= 1

             if i<=j:
                x = self.vec[i]^self.vec[j]
                self.vec[i] = x^self.vec[i]
                self.vec[j] = x^self.vec[j]   
                i += 1
                j -= 1

          if li < j:
             self._quicksort(li, j) 

          if i < ls:
             self._quicksort(i, ls) 

        
      def get(self):

          return self.vec      

#defined an array 
arr = [9,8,7,6,5,4,3,2,1,0]

#created an object
ob = QuickSort( arr )

#print the sorted array
print ob.get();