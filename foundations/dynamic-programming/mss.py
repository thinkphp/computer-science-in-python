import sys

class MaxSubSum:

	  arr = []
	  len = 0

	  def __init__(self, arr = 0):

	  	  #self.read()
	  	  n = int(sys.stdin.readline())
	  	  line = sys.stdin.readline()
	  	  line = line.split("\n")[0]
	  	  seq = line.split(" ")
	  	  self.arr = [0] * n	  	  
	  	  for i in range(0, n):
	  	  	  self.arr[i] = int(seq[i])
	  	  # for debug	  
	  	  #print self.arr 	         
	  	  self.len = n   
	  	  self.dynamic_programming()

	  def read(self):
	  	  f = open('ssm.in','r')
	  	  lines = f.readline()
	  	  self.len = int(lines)
	  	  self.arr = [0] * int(lines)
	  	  our_seq = f.readline().split("\n")
	  	  our_seq = our_seq[0].split(" ")
	  	  for i in range(0, int(lines)):
	  	  	  self.arr[i] = int(our_seq[i])
	  def dynamic_programming(self):
	      start = 0
	      end = -1
	      possibleStart = 0
	      maxsum = self.arr[0]
	      currentSum = 0

	      for i in range(0, self.len):
	      	  if currentSum < 0:
	      	     possibleStart = i 
	      	  currentSum = max(currentSum + self.arr[i], self.arr[i])
	      	  if currentSum > maxsum:
	      	  	  maxsum = currentSum
	      	  	  start = possibleStart
	      	  	  end = i
	      print maxsum, start + 1, end + 1	  	  
	      #self.write(maxsum,start+1,end+1)

	  def write(self, maxsum, start, end):
	      f = open('ssm.out','w')
	      f.write(str(maxsum))
	      f.write(' ')
	      f.write(str(start))
	      f.write(' ')
	      f.write(str(end))
	      f.close()
	   
ob = MaxSubSum()
