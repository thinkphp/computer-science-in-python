import math
nl = list(input().split(' '))
a = int(nl[0])
b = int(nl[1])
c = int(nl[2])
 
if a == 0 and b == 0:
	if c != 0:
		print(0)
		exit()
	print(-1)
	exit()
	
if a == 0:
	print(1)
	print("%10.5f" % (-c/b))
	exit()
	
sqrt = b*b - 4*a*c
if sqrt == 0:
	print(1)
	print("%10.5f" % (-b/2/a))
elif sqrt < 0:
	print(0)
else:
	print(2)
	roots = [(math.sqrt(sqrt)-b)/2/a, (-math.sqrt(sqrt)-b)/2/a]
	roots.sort()
	print("%10.5f" % roots[0])
	print("%10.5f" % roots[1])
