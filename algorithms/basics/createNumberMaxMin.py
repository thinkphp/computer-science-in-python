def concatMaxMin(arr):
    maxim = max(arr)
    minim = min(arr)
    x = maxim
    y = minim
    while y:
        x = x * 10
        y //=10
    return x + minim
def fn():
    arr = [10,552,1,11,888,40,24,2]
    n = concatMaxMin(arr)
    print(n)
fn()
