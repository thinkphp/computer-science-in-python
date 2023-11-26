# algoritmul lui Euclid iterative
def euclid_it(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

# algoritmul lui Euclid recursive
def euclid_rec(a, b):
    if b == 0:
        return a
    else:
        return euclid_rec(b, a % b)

# cifra de control version1
def ControlDigit1( a ):
    if a % 9 != 0:
        return a % 9
    else:
        return 9
# cifra de control version2
def ControlDigit2( a ):

    while a > 9:
        sum = 0
        while a > 0:
            sum += a % 10
            a //= 10
        a = sum
    return sum
def swap(v,a,b):
    aux = v[a]
    v[a] = v[b]
    v[b] = aux

def sorting(v):
    for i in range(0, len(v)-1):
        for j in range(i + 1, len(v)):
            if v[i] > v[j]:
                swap(v, i, j)
