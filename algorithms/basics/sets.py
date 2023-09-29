class Set:
    def __init__(self, n):
        self.n = n
        self.set = [0]*(1000)
def read():
    n = int(input("n="))
    A = Set(n)
    for i in range(0, n):
        A.set[i] = input("elem=")
    return A

def printf(set):
    for i in range(0,set.n-1):
        print(set.set[i], end = ", ")
    print(set.set[set.n-1])

def belong(set, elem):
    ok = False
    for i in range(0, set.n):
        if elem == set.set[i]:
            ok = True;
            break;
    return ok


def main():
    A = read()
    print("Set A:")
    printf(A)
    B = read()
    print("Set B:")
    printf(B)
    I = []
    D = []
    R = B
    for index in range(0, A.n):
        if belong(B, A.set[index]) is True:
            I.append(A.set[index])
        else:
            D.append(A.set[index])
            R.set[R.n] = A.set[index]
            R.n =R.n + 1
    print("Intersection:")
    print(I)
    print("Difference")
    print(D)
    print("Union:")
    printf(R)
main()
