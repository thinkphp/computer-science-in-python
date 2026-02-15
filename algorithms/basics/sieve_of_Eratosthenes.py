def ciur_version1(n):
	sieve = [0] * (n+1)
	size = n - 1
	i = 2
	while i * i <= n:
	  if not sieve[i]:
	  	 j = 2
	  	 while i * j <= n:
	  	 	multiply = i * j
	  	 	if sieve[multiply] == 0:
	  	 		size -=1
	  	 	sieve[multiply] = 1
	  	 	j+=1
	  i+=1
	return size  

def ciur_version2( n ):

    sieve = [0] * (n+1)
    cnt = 0
    i = 2

    while i * i <= n:
      if sieve[i] == 1:
      	i+= 1
      	continue
      j = 2 * i
      while j <= n:	
      	if not sieve[j]:
      	   sieve[j] = 1
      	   cnt+=1
      	j += i
      i += 1    	

    return n - cnt - 1

def main():
    n = int(input("n = "))
    print(ciur_version1(n))
    print(ciur_version2(n))

if __name__ == '__main__':
	main()
	
