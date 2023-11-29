def fta( n ):
    i = 2
    while not (n == 1):
        fm = 0
        while n % i == 0:
            fm += 1
            n //= i
        if fm:
            print(f"{i} * {fm}")
        i += 1
 
def main():
    print("Fundamental Theorem of Arithmentic")
    n = int(input("N = "))
    fta( n )
main()
