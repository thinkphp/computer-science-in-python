input()
s=[int(i) for i in input().split()]
a=max(s)
k=[]
for i in s:
    if a%i!=0 or s.count(i)==2:
        k.append(i)
print(a,max(k))
