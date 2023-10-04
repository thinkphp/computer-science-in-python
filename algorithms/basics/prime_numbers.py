def sqrt(n):
    x = n
    y = 1.0
    e = 0.0000001
    while x - y > e:
        x =  (x + y) / 2
        y = n / x
    return x

def isPrime(n):
    prime = True
    i = 2
    if(n <= 1): return False
    if(n == 2 or n == 3): return True
    while i <= sqrt(n) and prime is True:
        prime = n % i != 0
        i+= 1
    return prime

def main():
    count = 0
    i = 2
    n = int(input("n = "))
    while count != n:
        if isPrime(i) is True:
           if count == n - 1:
              print(i,end="")
           else:
              print(i, end=",")
           count+=1
        i += 1
main()
