#Most discussions tent to end up with Quick Sort Algorithm
class QuickSort:

  #define public vector to get array from input
  vec = [] 

  #defined length of the array
  len = -1

  #A little variable on which we store the pivot of the vector and first time we set to -1
  #to the left of the pivot p we have numbers less than p and to the right we have elements greater than p
  p = -1

  #constructor of the class 
  def __init__(self, arr):

        self.vec = arr
        self.len = len(self.vec)

  #public method getter
  def get(self):
      return self.vec  

  #public method setter
  def set(self,arr):
      self.vec = arr

  #public method sort
  def sort(self):
      self._qs(0,self.len-1)

  #private method finding the pivot
  def partition(self,li,ls):

      i = li
      j = ls
      i1 = 0
      j1 = -1
     
      aux = 0

      while i<j:

            if self.vec[i] > self.vec[j]:

               self._swap(i,j)  

               aux = i1
               i1 = -j1
               j1 = -aux

            i = i + i1
            j = j + j1

      self.p = i    



  #private method doing divide et impera
  def _qs(self,li,ls):

    if li<ls:

      self.partition(li,ls)  
      self._qs(li,self.p-1) 
      self._qs(self.p+1,ls)  


  #private method additional helper function to interchange some elements from different positions
  def _swap(self,i,j):
      temp = self.vec[i]
      self.vec[i] = self.vec[j]
      self.vec[j] = temp   
 
#let's take this vector as input
arr=[9,8,7,6,5,4,3,2,1]

#create an object of this class QuickSort
ob = QuickSort(arr)

#called sort method
ob.sort()

#and finally get the sorted array for quod erat demonstrandum
print ob.get()       

