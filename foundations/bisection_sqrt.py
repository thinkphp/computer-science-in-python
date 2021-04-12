def f(x, a):

    return x * x - a

def bisection(lo, hi, a):

    EPS = 0.00001

    while not hi - lo <= EPS:

        m = (lo + hi) / 2

        print(f'[{lo}, {hi}]', lo, hi)

        if f(lo, a) * f(m, a) < 0:

            hi = m

        else:

            lo = m

    return m

def bisection2(lo, hi, a):

    EPS = 0.00001

    while not hi - lo <= EPS:

        m = (lo + hi) / 2

        x = lo * lo - a
        y = m * m - a

        print(f'[{lo}, {hi}]')

        print()

        if (x > 0 and y < 0) or (x < 0 and y > 0):

            hi = m

        else:

            lo = m

    return hi

def main():

    n = int(input())

    res = bisection2(0, n + 5, n)

    print(res)
main()
