def printf(peak):
    for i in range(1, peak + 1):
        print(stack[i], end = " ")
    print("")

def back(peak):
    x = stack[peak - 1] + 1
    while x <= n:
        stack[peak] = x
        printf(peak)
        back(peak + 1)
        x += 1

def display():
    k = 0
    for i in range(1, n + 1):
        k = 1
        if used[ i ] == 1:
                print( i , end = " ")
        if k == 1:
            continue
    if k == 1:
        print("")

def bk(level):
    if level == n + 1:
        display()
    else:
      used[level] = 0
      bk(level + 1)
      used[level] = 1
      bk(level + 1)

def subsets(m):
    global n, used
    used = [0] * 100
    n = m
    bk(1)

#subsets(3)
def main():
    global n, stack
    n = 3
    stack = [0] * 20
    back(1)
main()
