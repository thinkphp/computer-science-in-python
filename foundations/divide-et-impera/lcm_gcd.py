def lcm(a, b):
    return a*b//g_c_d(a,b)
def l_m_c(arr):
    l = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        l = lcm(l,arr[i])
    return l

def g_c_d(a,b):
        while a!=b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

def divide_et_impera3(lo, hi, arr):
    if lo == hi:
        return arr[lo]
    else:
        middle = (lo + hi) >> 1
        a = divide_et_impera3(lo, middle, arr)
        b = divide_et_impera3(middle+1, hi, arr)
        return g_c_d(a,b)
def gcd(arr):
    return divide_et_impera3(0, len(arr)-1, arr)

def divide_et_impera2(lo, hi, arr):
    if lo == hi:
        return arr[lo]
    else:
        middle = (lo + hi) >> 1
        a = divide_et_impera2(lo, middle, arr)
        b = divide_et_impera2(middle+1, hi, arr)
        if a < b:
            return a
        else:
            return b
def min(arr):
    return divide_et_impera2(0, len(arr)-1, arr)

def divide_et_impera(lo, hi, arr):
    if lo == hi:
        return arr[lo]
    else:
        middle = (lo + hi) >> 1
        a = divide_et_impera(lo, middle, arr)
        b = divide_et_impera(middle+1, hi, arr)
        if a > b:
            return a
        else:
            return b
def max(arr):
    return divide_et_impera(0, len(arr)-1, arr)

def babylon(n):
    x = n
    y = 1
    e = 0.000001
    while x - y > e:
        x = (x + y) / 2
        y = n / x
    result = "sqrt(%d) = %f" % (n,x)
    print(result)
babylon(3)
def fact_dei(lo, hi):
    if lo == hi:
        return lo
    m = (lo + hi) >> 1
    a = fact_dei(lo, m)
    b = fact_dei(m+1,hi)
    return a * b

def fact(n):
    return fact_dei(1, n)
    
def mesopotamiam():
    arr = [12,14]
    print("max=%d"%max(arr))
    print("min=%d"%min(arr))
    print("gcd=%d"%gcd(arr))
    print("lcm=%d"%l_m_c(arr))
    print(fact(5))
mesopotamiam()
