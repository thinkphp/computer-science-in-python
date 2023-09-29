def main():
    n = 10000
    sieve = [1]*50000
    i = 2
    while i*i<=n:
        if sieve[i] == 1:
            j = 2
            while i*j<=n:
                sieve[i*j] = 0
                j+=1
        i+=1
    for i in range(2,n+1):
        if sieve[i]==1:
            print(i, end=" ")
main()
