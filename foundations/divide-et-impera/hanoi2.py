def _hanoi(n, a, b, c):
    if n == 1:
        hanoiSol.append([a,b])
    else:
        _hanoi(n-1,a,c,b)
        hanoiSol.append([a,b])
        _hanoi(n-1,c,b,a)

def func():
    global hanoiSol
    hanoiSol = []
    _hanoi(3,'a','b','c')
    for x,y in hanoiSol:
        print("(",x,y,")")
func()
