def init():
    global stack, level

    if level == 1:
       stack[level] = 0
    else:
       stack[level] = stack[ level - 1 ] - 1

def valid():
    global stack, level, N, sum

    if stack[level] <= N - sum:
       sum += stack[level]
       return True;
    return False

def succ():
    global stack, level, N, sum

    if stack[level] < N - sum:
       stack[level] += 1
       return True
    else:
       sum -= stack[level-1]
       return False

def printf():
    global stack, level, sum

    for i in range(1, level + 1):
        print(stack[i], end = ' + ')
    sum -= stack[level]
    print("\b\b ", end="")
    print()

def sol():
    global sum, N
    return sum == N

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
             else:
                 level += 1
                 init()
          else:
              level -= 1


def main():
    global N, sum, stack
    N = 10
    stack = [0] * (N + 1)
    sum = 0
    bk()
main()
