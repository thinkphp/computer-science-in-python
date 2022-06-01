def isPrime(n): 
 
    prime = True
    i = 2
    while i * i <= n and prime is True:
          prime = n % i != 0
          i += 1  
 
    return prime
 
def goldbach( n ):
 
   out = ""
 
   for i in range(2, n // 2 + 1):
 
 
       if isPrime(i) is True and isPrime(n - i) is True:
 
          out += "%d + %d = %d \n" % (i, n - i, n)
 
   return out
 
 
def main():
 
   arr = [100, 200, 300, 20, 51, 102, 7]
 
   for i in arr:
 
       print(goldbach(i))
 
main()   
