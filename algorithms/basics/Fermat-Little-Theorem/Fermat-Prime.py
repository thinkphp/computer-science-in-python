import random

def check(n):

    if n == 2 or n == 3:

    	return True

    if n < 2:

        return False

    if n & 1 == 0:

       return False

    prime = True

    i = 3

    while i * i <= n and prime:

      prime = (n % i) != 0

      i += 2

    return prime

def fast_pow(base, exp, mod):

    res = 1

    while exp > 0:

      if exp & 1:

         res = (res * base) % mod

      base = (base * base ) % mod

      exp >>=1

    return res

# Fermat's Little Theorem
# if p is Prime then it exits a number p, 1 < p < a, such us
# a^p-1 = 1 MOD p

def Fermat(n):

    if n < 2:
        return False

    if n in (2,3):

        return True

    if n % 2 == 0:
        return False

    for i in range( 10 ):

        a = random.randrange(2, n-1)

        if fast_pow(a, n - 1, n ) != 1:

            return False

    return True # is probably True

def main():
    n = int(input("N = "))
    print("the number: ", n)
    print("Brute Force: ", end="")
    if check( n ) is True:
        print("is Prime")
    else:
        print("is Not Prime")
    print("Fermat Test: ", Fermat( n ))
main()
