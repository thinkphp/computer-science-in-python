# Factorial using the methods
#  - Divide Et Impera
#  - Recursive
#  - Iterative
# n = 5
# n! = 5!
# fact = 1 * 2 * 3 * 4 * 5

def fact_dei(lo, hi):
    if lo == hi:
        return lo
    else:
        m = (lo + hi) >> 1
        a = fact_dei(lo, m)
        b = fact_dei(m+1, hi)
        return a * b

def fact_rec(n):
    if n == 0:
       return 1
    else:
        return n * fact_rec(n - 1)

def fact_it(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p

def main():
    n = 10
    res = fact_dei(1, n)
    print(res, end =' < -- > ')
    print(fact_rec(n), end =' < -- > ')
    print(fact_it(n), end = '')
main()
