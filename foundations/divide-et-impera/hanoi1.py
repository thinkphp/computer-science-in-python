def hanoi(n, a, b, c):
    if n == 1:

        print('(',a, b,')', end = " ")

    else:
        hanoi(n - 1, a, c, b)
        print('(',a, b,')', end = " ")
        hanoi(n - 1, c, b, a)

def towers(n):

    hanoi(n, 'a', 'b', 'c')
towers(3)
