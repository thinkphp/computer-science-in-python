def qs(lo, hi, arr):
	
	i = lo
	
	j = hi
	
	m = arr[(lo+hi)>>1]
	
	while i <= j:
		
		while arr[i] < m:
			i+=1
		while arr[j] > m:
			j-=1
		if i <= j:
			arr[i],arr[j] = arr[j],arr[i]
			i+=1
			j-=1
	if lo < j:
		qs(lo, j, arr)
	if i < hi:
		qs(i, hi, arr)
	
def main():
	
	arr = [4,5,6,7,8,9,9,2,3,3,4,4,4,3,2,2,1,1,1,1,8]
	
	n = len( arr )
	
	qs(0, n-1, arr )
	
	print(arr)
	
	vec = [0] * (n+1)
	
	freq = [0] * (n+1)
	
	k = 0
	
	vec[k] = arr[k]
	
	freq[k] = 1
	
	for i in range(n-1):
		if arr[i] == arr[i+1]:
			freq[k]+=1
		else:
			k += 1
			vec[k] = arr[i+1]
			freq[k] = 1
	for i in range(0, k+1):
		if freq[i] == 1:
			print("%d appears one time" % (vec[i]))
		else:
			print("%d appears %d times" % (vec[i], freq[i]))
main()	
