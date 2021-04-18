def init():
    global stack, level
    stack[level] = 0

def succ():
    global stack, level, N

    if stack[level] < N:
       stack[level] += 1
       return True
    return False

def valid():
    global stack, level

    for i in range(1, level):
        if abs(stack[i] - stack[level]) == abs(i - level) or (stack[i] == stack[level]):
           return False
    return True


def sol():
    global level, N
    return level == N

def printf():
    global stack, N, mat
    for i in range(1, level + 1):
        mat[i][stack[i]] = 1
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            print(mat[i][j],  end = ' ')
        print()

def bk():
    global level
    level = 1
    init()

    while not level == 0:
        hs = True
        iv = False
        while hs is True and iv is False:
              hs = succ()
              if hs is True:
                 iv = valid()

        if hs is True:
            if sol() is True:
                printf()
                break
            else:
                level += 1
                init()
        else:
            level -= 1

def main():
    global N, stack, mat

    N = 8
    mat = []
    for i in range(0, N + 1):
        arr = []
        for j in range(0, N + 1):
            arr.append( 0 )
        mat.append( arr )

    stack = [ 0 ] * (N + 1)
    bk()


main()
