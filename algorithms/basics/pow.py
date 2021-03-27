def pow2(b, exp):
	ans = 1
	while exp!=0:
		if exp % 2:
		   ans = ans * b
		b = b * b
		exp = int(exp // 2)	
	return ans

print(pow2(2,10))
