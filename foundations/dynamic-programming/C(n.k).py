#
# Finding Comb(n,k) using Dynamic Programming
#
def fn():
      n = 100
      k = 4
      rows = n
      cols = k
      C = [[0 for _ in range(rows+1)] for _ in range(rows+1)]
      C[0][0] = 1
      for i in range(1, n+1):
          for j in range(0, i+1):
              if 0 == j or i == j:
                 C[i][j] = 1
              C[i][j] = C[i-1][j-1] + C[i-1][j]
      for i in range(0, n+1):
          for j in range(0, i+1):
              print(C[i][j],end=" ")
          print()
      print(C[10][6])
fn()
