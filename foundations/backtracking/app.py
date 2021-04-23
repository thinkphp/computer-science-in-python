class Element:

      def __init__(self,x,y):
          self.x = x
          self.y = y

Dist = [(0,0), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]

def init():

    global p, level

    p[ level ] = 0

def succ():

    global level, stack, p

    if p[level] < 8:
       p[level] += 1
       stack[level].x = stack[level-1].x + Dist[p[level]][0]
       stack[level].y = stack[level-1].y + Dist[p[level]][1]
       return True
    return False

def valid():
    global stack, level, N

    if stack[level].x < 1 or stack[level].x > N or stack[level].y < 1 or stack[level].y > N:

       return False

    for i in range(1, level):

        if stack[i].x == stack[level].x and stack[i].y == stack[level].y:
           return False

    return True

def bk():

    global level
    level = 2
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
               break
           else:
               level +=1
               init()
        else:
           level -=1

def sol():

    global level, N

    return level == N * N

def printf():

    global stack, N

    for i in range(1, N*N+1):

        print('[', stack[i].x, stack[i].y, ']', end = ' ')

        for j in range(1, N + 1):

            if i == j * N:

               print()

def main():

    global level, N, stack, p

    N = 6

    p = [ 0 ] * ( N * N + 1 )

    stack = [ 0 ] * ( N * N + 1 )

    stack[ 1 ] = Element(1, 1)

    for i in range(2, N * N + 1):

        stack[i] = Element(0, 0)

    bk()

main()
