a, b, c = map(int, input().split())
 
if a < 0:
    a = -a
    b = -b
    c = -c
 
x = (b**2)-(4*a*c)
if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        print(1)
        print(f'{-c*1.0/b:.7f}')
elif x == 0:
    print(1)
    print(f'{-b/(2*a):.7f}')
elif x > 0:
    from math import sqrt
 
    x = sqrt(x)
 
    a1 = (-b-x)/(2*a)
    a2 = (-b+x)/(2*a)
    print(2)
    print(f'{a1:.7f}')
    print(f'{a2:.7f}')
else:
    print(0)
