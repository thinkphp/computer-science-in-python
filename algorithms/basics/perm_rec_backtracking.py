def init(level):
    st[level] = 0

def succ(level):
    if st[level] < n:
        st[level] +=1
        return True
    return False

def valid(level):
    for i in range(0, level):
        if st[level] == st[i]:
            return False
    return True

def sol(level):
    return level == n

def printf():

    for i in range(1,n+1):
        print(st[i], end = " ")
    print()

def bk(level):
    init(level)
    while succ(level):
        if valid(level):
            if sol(level):
                printf()
            else:
                bk(level+1)
def cebu():
    global st, n
    n = 3
    st = [0] * (n+1)
    bk(1)
cebu()
