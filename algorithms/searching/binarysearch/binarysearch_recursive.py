import unittest

def BinarySearch(arr, key):

    if len(arr) == 0:

        return False
 
    else:

        mi = len(arr)//2

        if key == arr[ mi ]:

           return True

        else:

            if key < arr[ mi ]:

               return BinarySearch(arr[:mi], key)

            else:

               return BinarySearch(arr[mi+1:], key)

class BinarySearchTest(unittest.TestCase):

      def test_basic(self):
 
          arr = [1,2,3,4,5,6,7,8,9]

          for i, n in enumerate(arr):

              self.assertEquals(BinarySearch(arr, n), True) 


      def test_missing(self):
 
          arr = [1,2,3,4,5,6,7,8,9]

          self.assertEquals(BinarySearch(arr, 19), False) 

      def test_odd(self):
 
          arr = [2,4,6,8,10,12,14]

          for i, n in enumerate(arr):

              self.assertEquals(BinarySearch(arr, n), True) 

      def test_even(self):
 
          arr = [1,3,5,7,9,11,13,17]

          for i, n in enumerate(arr):

              self.assertEquals(BinarySearch(arr, n), True) 

      def test_empty(self):

          arr = []

          self.assertEquals(BinarySearch(arr, 19), False) 

if __name__ == '__main__':

   unittest.main()  

   
