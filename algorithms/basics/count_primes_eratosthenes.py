def main():
    n = 10
    SIZE = 1000
    sieve = [1]*SIZE
    i = 2
    count = n-1
    while i*i<=n:
        if sieve[i] == 1:
            j = 2
            while i*j<=n:
              if sieve[i*j]:
                 count-=1
              sieve[i*j] = 0
              j+=1

        i+=1
    print("Primes:", end = " ")
    for i in range(2,n+1):
        if sieve[i]==1:
            print(i, end = " ")
    print("\nCount :",count)
main()
