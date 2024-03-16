n=int(input())
l=list(map(int,input().split()))
l.sort();s=0
for i in range(1,n,2):
	s+=(l[i]-l[i-1])
print(s)
