def main():
    def isOne(n,p):
        return (n>>p)&1
    def isPrime(n):
        return not isOne(sieve[n//8],n%8)
    size = 1000
    sieve = [0]*(size//8+1)
    n = 100
    i = 2
    while i*i<=n:
        if isOne(sieve[i//8],i%8) == 0:
           j = 2
           while i*j<=n:
               aux = 1
               aux <<= (i*j)%8
               sieve[(i*j)//8] |= aux
               j+=1
        i+=1
    for i in range(2,100):
        print(i, end = "--> ")
        if isPrime(i):
            print("Prime", end =" ")
        else:
            print("Compound", end = " ")
        print()
main()
