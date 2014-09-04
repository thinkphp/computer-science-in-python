class Mergesort:

      #defined a vector 
      vec = []

      #start with length -1
      len = -1

      #constructor of the class
      def __init__(self,arr):

          self.vec = arr

          self.len = len(arr)

      #public method sort
      def sort(self):

          self._divimp(0,self.len-1)

      #merge private method used in divide et impera
      def _merge(self,li,m,ls):

          i = li
          j = m+1

          k = 0
          temp = []
          for q in range(0,self.len):
              temp.append(0)

          while i<=m and j<=ls:

              if self.vec[i]<self.vec[j]:
                 temp[k] = self.vec[i]
                 k = k + 1
                 i = i + 1
              else:
                 temp[k] = self.vec[j]
                 k = k + 1
                 j = j + 1

          if i<=m:
             for w in range(i,m+1):
                 temp[k] = self.vec[w]   
                 k = k + 1

          if j<=ls:
             for w in range(j,ls+1):
                 temp[k] = self.vec[w]
                 k = k + 1

          k = 0
          for i in range(li,ls+1):
              self.vec[i] = temp[k]
              k = k + 1

      
      #private method using divide and impera style
      def _divimp(self,li,ls):

          if((ls-li)<=1):
              self.swap(li,ls)
          else:
              m = (li+ls)/2
              self._divimp(li,m)
              self._divimp(m+1,ls)
              self._merge(li,m,ls)

      def swap(self,i,j):

          if self.vec[i] > self.vec[j]:

              temp = self.vec[i]
              self.vec[i] = self.vec[j]
              self.vec[j] = temp  

      #@public
      #display the array
      def get(self):
          return self.vec 

arr = [9,8,7,6,5,4,3,2,1,-1,111,-1221,0,12]
obj = Mergesort(arr)
obj.sort()
print obj.get()
         