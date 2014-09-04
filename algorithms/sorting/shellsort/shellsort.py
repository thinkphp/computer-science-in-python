class Shellsort:

      #declare an empty array
      vec = []

      #start with the length -1
      len = -1

      #constructor of the class
      def __init__(self, arr=[]):

          if len(arr) is not 0:

             self.vec = arr

             self.len = len(arr)

      #public method sort
      def sort(self):

          dist = [7, 5, 3, 1]

          N = self.len
          print N

          for d in range(0, len( dist )):

              the_dist = dist[ d ]
             
              for i in range(the_dist, N):

                  aux = self.vec[ i ]

                  j = i - the_dist

                  while j >= 0 and self.vec[j] > aux:

                        self.vec[ j + the_dist] = self.vec[ j ]

                        j = j - the_dist

                  self.vec[ j + the_dist ] = aux 

                        
      #read from file.in  
      def read(self):

          #get a handler from file
          fin = open('shellsort.in', 'r')

          vec = [] 

          #get the number of the items from array which is stored in the first line of the file and convert it to integer from string
          n = int( fin.readline() )

          #get the next line and convert them into integers from string
          arr = fin.readline() 
          
          #split " "
          arr = arr.split(" ")

          #walk through array and append
          for i in range(0, n - 1):

              vec.append(int(arr[i]))

          #assign the length 
          self.len = len(vec)

          #assign the array read
          self.vec = vec

      #write to File.out
      def write(self):

          fout = open('shellsort.out','w')

          fout.write(str(self.get()))  

          fout.close()

      #return the array
      def get(self):

          return self.vec 

ob = Shellsort()

ob.read()
ob.sort()
ob.write()

print ob.get()
         