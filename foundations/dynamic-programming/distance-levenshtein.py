arr = list(map(str, input().split()))
a = arr[0]
b = arr[1]
# Declaring array 'D' with rows = len(a) + 1 and columns = len(b) + 1:
D = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
 
# Initialising first row:
for i in range(len(a) + 1):
    D[i][0] = i
 
# Initialising first column:
for j in range(len(b) + 1):
    D[0][j] = j
 
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            D[i][j] = D[i - 1][j - 1]
        else:
            # Adding 1 to account for the cost of operation
            insertion = 1 + D[i][j - 1]
            deletion = 1 + D[i - 1][j]
            replacement = 1 + D[i - 1][j - 1]
 
            # Choosing the best option:
            D[i][j] = min(insertion, deletion, replacement)
 
print(D[len(a)][len(b)])
