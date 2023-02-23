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

 filepath = "colorphoto.in"

 with open(filepath) as fp:

   lines = fp.readlines()

   content = [x.strip() for x in lines]

 lineCol = content[0].split(" ")

 n = int(lineCol[0])

 m = int(lineCol[1])

 content.pop(0)

 matrix = []

 for element in content:

     line = element.split(" ")
     line = [int(x) for x in line]
     matrix.append(line)

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
