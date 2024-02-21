'''
Se citesc numerele naturale n1 si n2. Sa se calculeze produsul lor,
fara a utiliza operatorul de inmultire. (doar o structura repetetitiva)

n1 = 3
n2 = 4

3 + 3 + 3 + 3
adunam 3 la o variabila initiata cu zero de patru ori

print(n1 * n2)

intreg n1, n2, s, i

s <-- 0

i <-- 1

cat timp i <= n2 executa
    s <--- s + n1
    i = i + 1

Scrie s
'''

def inmultire():
    n1 = int(input("n1="))
    n2 = int(input("n2="))
    s = 0
    i = 1
    #n1 = 2
    #n2 = 4
    # 2 + 2 + 2 + 2

    # i = 1
    # 5 <= 4 NU

    while i <= n2:

        s = s + n1 # s = 6 + 2 = 8
        i = i + 1  # i = 4 + 1 = 5 GO TO line 37

    print("n1 * n2 = ", s)

inmultire()
