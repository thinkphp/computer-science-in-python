# with tail recursion
def fib(n, a, b):
 
    if n == 0:
 
        return a
 
    else:
        print(a, end = ' ')
 
        return fib(n - 1, b, a + b)
def main():
    n = 10
    nth = fib(n, 0, 1)
    print(nth)
main()
