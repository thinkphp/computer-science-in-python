def _tobin(n):
 
    for i in range(15, -1, -1):
 
    	print((n>>i)&1, end='')
    	
def _tobin_(n):
 
	out = [] 
 
	while n:
 
	  out.append(n%2)
 
	  n //= 2
 
	print(''.join(str(i) for i in out[::-1]))
	
def tobin(n):

	if n // 2 > 0:

	   tobin(n // 2)

	print(n % 2, end = '')

def _pow(a, b):

	p = 1
	
	for i in range(1, b + 1):
	
		p *= a
		
	return p

def toDec( n ):

	base = 0
	dec = 0

	while n > 0:
		dec += n % 10 * _pow(2, base)
		base += 1
		n //= 10

	print(dec)

def main():
        tobin(8)
        print()
        _tobin(8)
        print()
        _tobin_(8)
        print()
        toDec(1000)

main()
