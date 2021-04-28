# factorial with tail recursion
def fact(n, a):
    if n == 1:
 
       return a
 
    else:
 
       return fact(n - 1, n * a)
 
def main():
    n = 200
    print(fact(n, 1))
main()
