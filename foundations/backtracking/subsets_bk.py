def func():
    def display(level):
        for i in range(1, level+1):
            print(stack[i], end = " ")
        print()

    def subsets(level):
        if level <= n:
            for i in range(stack[level-1]+1,n+1):
                stack[level] = i
                display(level)
                subsets(level+1)

    n = 3

    stack = [0] * (n+1)

    subsets(1)

func()
