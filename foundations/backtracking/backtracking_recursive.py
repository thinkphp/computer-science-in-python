def init(level):

    global stack
    stack[ level ] = 0

def succ(level):

    global n, stack

    if stack[ level ] < stack[ level - 1] + 1:

       stack[ level ] += 1
       return True

    return False

def valid(level):

    return True

def sol(level):

    global n
    return level == n

def printf():

    global n, stack

    mx = max(stack)
    for i in range(1, mx + 1):
        print('{', end='')
        for j in range(1, n + 1):
            if stack[ j ] == i:
               print(j, end = ',')
        print('\b}', end='')
    print()

def bk(level):

    init(level)
    while succ(level) is True:
        if valid(level) is True:
            if sol(level) is True:
                printf()
            else:
                bk(level + 1)

def main():
    global stack, n
    n = 3
    stack = [0] * (n + 1)
    bk(1)
main()
