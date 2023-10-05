from sys import getsizeof
def sqrt(n):
    x = n
    y = 1
    eps = 0.00001
    while x - y > eps:
        x = (x+y)/2
        y = n / x
    return x

def isPrime(n):
    if n<=1:return 0
    if n == 2 or n == 3: return 1
    prime = True
    for i in range(2,int(sqrt(n))+1):
        if prime == False:
            break
        prime = (n%i) != 0
    return prime

def bin(num):
    n = getsizeof(num)
    for i in range(n,-1,-1):
        if (num>>i)&1:
            print(1,end="")
        else:
            print(0,end="")
    print()

def main():
    for num in range(1,1000):
        if isPrime(num):
           print(num,end=":")
           bin(num)
main()
