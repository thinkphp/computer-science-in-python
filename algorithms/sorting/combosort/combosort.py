class Algorithm:

      arr = []

      def __init__(self, arr):

          self.arr = arr

          self._qs()

      def _bs(self):

          n = len(self.arr)

          finished = False        

          while finished == False:

            swapped = False

            for i in range(0, n-1):

                if(self.arr[i] > self.arr[i+1]):

                      self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]

                      swapped = True

            if swapped == True:

               n = n - 1

            else:

               finished = True 

      def _cs(self):
 
          shrinkFactor = 1.3

          swapped = True

          gap = len(self.arr)

          while gap > 1 or swapped == True:

                swapped = False

                if gap > 1:

                   gap = int( gap / shrinkFactor )

                for i in range(len(self.arr) - gap):

                     if self.arr[i] > self.arr[i+gap]:

                        self.arr[i], self.arr[i+gap] = self.arr[i+gap], self.arr[i]

                        swapped = True  

      def _qs(self):

          def _qsort(L): 

              if len(L) <= 1: 

                 return L

              else:  

                 return _qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + _qsort([ge for ge in L[1:] if ge >= L[0]])
  
          self.arr = _qsort(self.arr) 

      def get(self):

          return self.arr

def _qsort(L):


     if len(L) <= 1: 

               return L

     else:  

               return _qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + _qsort([ge for ge in L[1:] if ge >= L[0]])
  


def main():

    f = open("algsort.in", "r")

    arr = []

    for val in f.read().split():

        arr.append(int(val))
 
    f.close()
     
    arr.pop(0)

    ob = Algorithm( arr )
      
    out = open('algsort.out','w')

    out.write(" ".join(map(str, ob.get())))     
 
if __name__ == "__main__":
 
   main();
