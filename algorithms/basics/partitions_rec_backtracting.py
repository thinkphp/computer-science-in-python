def init(level):
    st[level] = 0

def succ(level):
    if st[level]<st[level-1]+1:
        st[level]+=1
        return True
    return False

def sol(level):
    return level == n

def valid(level):
    return True

def printf():
    thismax = max(st)
    for i in range(1, thismax+1):
        print("{",end="")
        for j in range(1, n+1):
            if st[j] == i:
                print(j, end = ",")
        print("\b}",end="")
    print()

def bk(level):
    init(level)
    while succ(level) is True:
        if valid(level):
            if sol(level):
                printf()
            else:
                bk(level+1)



def Palawan():
    global st, n
    n=5
    st=[0]*(n+1)

    bk(1)
Palawan()
