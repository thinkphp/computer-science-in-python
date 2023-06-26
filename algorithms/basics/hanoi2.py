def h(d, s, a, t):
    if d == 1:
        print('{} {}'.format(s, t))
        return
 
    h(d - 1, s, t, a)
    print('{} {}'.format(s, t))
    h(d - 1, a, s, t)
 
n=int(input())
print(2**n-1)
h(n,'1','2','3')
