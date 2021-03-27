import sys
def toBin(n):
	size = 16
	for i in reversed(range(0, size)):
		print((n>>i)&1,end='')

def main():
    n = int(sys.argv[1])
    
    toBin(n)
main()  
