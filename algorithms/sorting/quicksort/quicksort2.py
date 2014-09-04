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

  def partition(self,li,ls):

      i = li
      j = ls
      
      pivot = self.vec[(li+ls)/2]      

      while i<=j:

         while self.vec[i] < pivot:
               i = i + 1
         while self.vec[j] > pivot:
               j = j - 1
         if i<=j:
            self.swap(i,j)
            i = i + 1
            j = j - 1

      return i  

  def _qs(self,li,ls):

      p = self.partition(li,ls)
      if p-1 > li:
         self._qs(li,p-1)
      if p < ls:
         self._qs(p,ls)  

  def swap(self,i,j):
      temp = self.vec[i]
      self.vec[i] = self.vec[j]
      self.vec[j] = temp   
 

arr=[9,8,7,6,5,4,3,2,1,-1,-3]

ob = QuickSort(arr)

print ob.get()       

