def coloring(i, j, color):

    global matrix

    if i >= 0 and j >= 0 and i < n and j < m and 1 == matrix[i][j]:

        matrix[i][j] = color

        coloring(i, j + 1, color)
        coloring(i, j - 1, color)
        coloring(i + 1, j, color)
        coloring(i - 1, j, color)

def func():

 global matrix, n, m

 matrix =[[4,6],[1,1,0,1,1,0],[1,1,0,0,0,1],[0,0,0,1,1,1],[1,1,0,0,1,0]]

 n = int(matrix[0][0])

 m = int(matrix[0][1])

 matrix.pop(0)

 for i in range(0, n):

     for j in range(0, m):

         print(matrix[i][j], end = " ")

     print(end = "\n")

 global color

 color = 2

 for i in range(0, n):

     for j in range(0, m):

         if matrix[i][j] == 1:

             coloring(i, j, color)

             color+=1

 print("\n")

 for i in range(0, n):

    for j in range(0, m):

        print(matrix[i][j], end = " ")

    print(end = "\n")

func()
