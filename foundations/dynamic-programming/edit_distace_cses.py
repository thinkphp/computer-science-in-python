word1 = input()
word2 = input()
 
m = len(word1)
n = len(word2)
table = [[0] * (n + 1) for _ in range(m + 1)]
 
for i in range(m + 1):
    table[i][0] = i
 
for j in range(n + 1):
    table[0][j] = j
 
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
            table[i][j] = table[i - 1][j - 1]
#                     if same move on
        else:
            table[i][j] = 1 + min(table[i - 1][j], table[i]
                                  [j - 1], table[i - 1][j - 1])
#             else check min of removing one from word1, one from word2, or both
print(table[-1][-1])
