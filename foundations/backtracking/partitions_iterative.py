def init():

    global stack, level
    stack[ level ] = 0

def succ():

    global n, level, stack

    if stack[ level ] < stack[ level - 1] + 1:

       stack[ level ] += 1
       return True

    return False

def valid():

    return True

def sol():

    global n, level
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

def bk():

    global stack, n, level
    level = 1
    init()

    while level > 0:

         hs = True
         iv = False

         while hs is True and iv is False:

               hs = succ()
               if hs is True:
                   iv = valid()

         if hs is True:

            if sol() is True:

               printf()

            else:

               level += 1
               init()
         else:
           level -= 1


def main():

    global stack, n
    n = 3
    stack = [0] * (n + 1)
    bk()

main()
