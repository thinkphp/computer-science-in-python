def divide(a, b):
    dividend = abs(int(a))
    divisor = abs(int(b))
    multiply = 1
    result = 0
    getsign = (a > 0 and b < 0) or (a < 0 and b > 0)
    if getsign is False:
        sign = 1
    else:
        sign = -1

    while dividend >= divisor:
        multiply = 1
        temp = divisor

        while temp<<1 <= dividend:

            multiply<<=1
            temp<<=1

        dividend-=temp
        result+=multiply

    return sign*result

def main():
    a = int(input("divident="))
    b = int(input("divisor = "));
    r = divide(a,b)
    print(r);

main()
