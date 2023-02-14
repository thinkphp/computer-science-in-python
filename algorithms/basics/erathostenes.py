def erathostenes(n):
    sieve = [True for i in range(n + 1)]
    i = 2
    size = n - 1
    while i * i <= n:
        if sieve[i] is True:
            j = 2
            while i * j <= n:
                multiply = i * j
                if sieve[multiply] is True:
                    size-=1
                sieve[multiply] = False
                j += 1
        i +=1
    output = []
    print(size)
    for i in range(2, n + 1):
        if sieve[i] is True:
            output.append(i)
    return output
def func():
    n = 10
    result = erathostenes(n)
    result = ", ".join(str(i) for i in result)
    print(result)
func()
