def Count1(n):
	cnt = 0
	while n:
	  x = n % 10
	  if x % 2 == 0:
	  	cnt+=1
	  n //=10
	return cnt
	
def Count2(n):
	cnt = 0
	while n:
	  x = n % 10
	  if x % 2 != 0:
	  	cnt+=1
	  n//=10	
	return cnt  	
	
def fn():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    even = odd = 0
    for i in arr:
    	if i == 0:
    		even+=1
    		continue
    	even += Count1(i)
    	odd += Count2(i)
    print(even, odd)
fn()    
