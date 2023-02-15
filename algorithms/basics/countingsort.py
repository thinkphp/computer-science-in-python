def func():
    a = [7,8,-5,3,2,1,-11]
    n = len(a)
    c = [0] * (n+1)
    b = [0] * (n+1)
    for i in range(0,n):
        c[i] = a[i]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                b[i]+=1
            else:
                b[j]+=1
    for i in range(n):
        a[b[i]] = c[i]
    print(a)
func()
