import sys

input = lambda : sys.stdin.readline().strip()

def solve(n, frm, to, middle, cnt, ans):

if n == 1:

ans.append((frm, to))

else:

solve(n - 1, frm, middle, to, cnt, ans)

ans.append((frm, to))

solve(n - 1, middle, to, frm, cnt, ans)

ans = []

solve(3, 1, 3, 2, 0, ans)

n = int(input())

if n == 1:

print(1)

print(1, 3)

elif n == 2:

print(3)

print(1, 2)

print(1, 3)

print(2, 3)

else:

ans = []

solve(n, 1, 3, 2, 0, ans)

print(len(ans))

for i in ans:

print(i[0], i[1])

# 1 3

# 1 2

# 3 2

# 1 3

# 2 1

# 2 3

# 1 3

