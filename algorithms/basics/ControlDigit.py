def Control1( n ):
    if n % 9 != 0:
        return n % 9
    else:
        return 9
def Control2( n ):
    while n > 9:
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        n = sum
    return sum
def main():
    n = int(input("n="))
    print(Control1(n))
    print(Control2(n))
main()
