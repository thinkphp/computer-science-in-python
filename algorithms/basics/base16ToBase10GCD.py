#
# Fundamentele Programarii. page 128.
# Se considera un sir de n numere scrise in baza 16.
# Sa se realizeze un program care determina cel mai mare
# divizor comun al acestor numere, afisandu-l in baza 10.
# In cadrul programului, vor fi definite si apelate doua
# programe:
# - conv function, care primeste un sir de caractere,
# reprezentand un numar in baza 16 si returneaza numarul
# obtinut in urma conversiei in baza 10
# - gcd function, care returneaza cel mai mare divizor comun
# a doua valori transmise prin intermediul a doi parametrii.
#
def power(a,b):

    p = 1

    for i in range(1,b+1):

        p = p * a

    return p

def val(c):

    if ord(c) >= ord('0') and ord(c) <= ord('9'):

        return ord(c) - ord('0')

    elif ord(c) >= ord('A') and ord(c) <= ord('Z'):

        return ord(c) - ord('A') + 10

def conv( str ):

    base = 16

    n = 0

    p = 0

    for i in range(len(str)-1, -1, -1):

        n = n + val((str[i])) * power(16, p)

        p += 1

    return n
def gcd(a,b):
    while a!=b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def func():

    n = int(input("N="))

    num = input("number1 = ")

    a = conv(num)

    for i in range(2,n+1):
         #convert to decimal
         b = conv(input("numnber%d = "%i))
         # greatest commond divisor
         a = gcd(a, b)

    print(a)

    vec = ["AA","BB","CC"]
    a = conv(vec[0])
    vec.pop(0)
    for i in vec:
        b = conv(i)
        a = gcd(a,b)
    print(a)

func()
