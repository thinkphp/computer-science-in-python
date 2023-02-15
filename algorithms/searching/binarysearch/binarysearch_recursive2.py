import unittest

"""
    Binary Search implemented in Python
    Assumes 'items' is a sorted list    
"""

def BinarySearch(arr, lo, hi, key):

    if lo > hi:
 
       return -1

    mi = (lo+hi)>>1  

    if key == arr[ mi ]:

       return mi
 
    if key < arr[mi]:

       return BinarySearch(arr, lo, mi - 1, key)

    else:

       return BinarySearch(arr, mi + 1, hi, key) 

class BinarySearchTest(unittest.TestCase):

      def test_basic(self):
 
          arr = [1,2,3,4,5,6,7,8,9]

          for i, n in enumerate(arr):

              self.assertEquals(BinarySearch(arr, 0, len(arr) - 1, n), i) 


      def test_missing(self):
 
          arr = [1,2,3,4,5,6,7,8,9]

          self.assertEquals(BinarySearch(arr,  0, len(arr) - 1, 19), -1) 

      def test_odd(self):
 
          arr = [2,4,6,8,10,12,14]

          for i, n in enumerate(arr):

              self.assertEquals(BinarySearch(arr, 0, len(arr) - 1, n), i) 

      def test_even(self):
 
          arr = [1,3,5,7,9,11,13,17]

          for i, n in enumerate(arr):

              self.assertEquals(BinarySearch(arr,  0, len(arr) - 1, n), i) 

      def test_empty(self):

          arr = []

          self.assertEquals(BinarySearch(arr,  0, len(arr) - 1, 19), -1) 

if __name__ == '__main__':

   unittest.main()  
    
   

   
   
 
