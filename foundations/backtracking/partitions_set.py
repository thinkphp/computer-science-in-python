class Backtracking:

	def init(self):

		self.stack[self.level] = 0

	def succ(self):

	    if self.stack[self.level] < self.stack[self.level - 1] + 1:	    	
	       self.stack[self.level] += 1
	       return True

	    return False   

	def valid(self):

		return True

	def sol(self):

	    return self.level == self.n	

	def print(self):
		_max = max(self.stack)
		for i in range(1, _max + 1):
			print("{", end = '')
			for j in range(1, self.n+1):
				if self.stack[j] == i:
					print(j, end =',')
			print("\b}", end = '')

		print()
         	
	def bk(self):
   
		self.level = 1
		self.init()
				
		while self.level > 0:

			succ = True
			while succ is True and self.valid() is True:
				succ = self.succ()
				if succ is True:
					break

			if succ is True:				
				if self.sol() is True:
					self.print()
				else:					
					self.level += 1
					self.init()
			else:				
				self.level -= 1       	      
		           

	def _getPartitions(self, n):
		
		self.bk()

	def __init__(self, n):

		self.n = n
		self.stack = [False] * (n + 1)			
		self._getPartitions(n)


def main():
    n = int(input("n="))
    ob = Backtracking(n)
main()    
