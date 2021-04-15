def init():

    global stack, level

    stack[ level ] = 0

def succ():

    global stack, level, k

    if stack[ level ] < n:

       stack[ level ] += 1

       return True

    return False

def sol():

    global level, k

    return level == k

def valid():

    global stack, level

    for i in range(1, level):

        if stack[ i ] == stack[ level ]:

            return False

    return True

def printf():

    global stack, k;

    for i in range(1, k + 1):

        print(stack[ i ], end = ' ')
    print()

def bk():

    global level

    level = 1
    init()

    while not level <= 0:

          hs = True
          iv = False

          while hs is True and iv is False:

                hs = succ()

                if hs is True:
                   iv = valid()

          if hs is True:

                if sol():
                      printf()
                else:
                      level += 1
                      init()
          else:
                level -= 1


def main():
    global n, k, stack
    #A = {1,2,3,4}
    n = 4
    k = 2
    stack = [ 0 ] * (k + 1)
    bk()
main()
