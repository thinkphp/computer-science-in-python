#public class quicksort
class QuickSort:

  #define public vector to get array from input
  vec = [] 

  #defined length of the array
  len = -1

  def __init__(self, arr):

        self.vec = arr
        self.len = len(self.vec)
        self.sort() 


  def get(self):
      return self.vec  

  def set(self,arr):
       self.vec = arr

  def sort(self):
      self._qs(0,self.len-1)

  def _qs(self,li,ls):

      p = self.partition(li,ls)
      if p+1<ls:
         self._qs(p+1,ls)
      if p-1>li:
         self._qs(li,p-1)

          
   
  def partition(self,li,ls):

      pivot = self.vec[ls]

      s = li - 1
      
      for i in range(li,ls+1):

          if self.vec[i] <= pivot:
             s = s + 1
             self.swap(s,i)

      return s

  def swap(self,a,b):

      temp = self.vec[a]
      self.vec[a] = self.vec[b]
      self.vec[b] = temp  
         
         
 

arr=[9,8,7,6,5,4,3,2,1,-1,-3]

ob = QuickSort(arr)

print ob.get()       

