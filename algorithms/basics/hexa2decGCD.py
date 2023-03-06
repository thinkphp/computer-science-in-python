def hexaGCD( x, y, z):

    def pow2(a,b):

        p = 1

        for i in range(1,b+1):
            p = p * a
        return p

    def val(c):

        if ord(c) >= ord('0') and ord(c) <= ord('9'):

            return ord(c) - ord('0')

        elif ord(c) >= ord('A') and ord(c) <= ord('Z'):

            return ord(c) - ord('A') + 10

    def conv(str):

        n = len(str)

        p = 0

        num = 0

        for i in range(n - 1, -1, -1):

            num = num + val(str[i]) * pow2(16, p)

            p += 1

        return num

    def gcd(a,b):

        while a!=b:

            if a > b:
               a = a - b
            else:
               b = b - a

        return a

    GreatestCommonDivisor = gcd(conv(x),conv(y))

    GreatestCommonDivisor = gcd(GreatestCommonDivisor, conv(z))

    return GreatestCommonDivisor

print(hexaGCD("AA","BB","CC"))
