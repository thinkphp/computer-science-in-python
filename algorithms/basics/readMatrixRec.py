import random
 
def readMatrixRec(matrix, k, p, cols):
    if k == p:
        for i in range(0, cols + 1):
            matrix[k][i] = random.randint(0, 1)
    else:
        for i in range(0, cols + 1):
            matrix[k][i] = random.randint(0, 1)
        readMatrixRec(matrix, k + 1, p, cols)
 
def main():
 
    lines = 3
    cols = 5
 
    # declara the matrix
    matrix = [[0 for j in range(0, cols)] for i in range(0, lines)]
 
    # read the elements(random /0/1) of the matrix
 
    # display the matrix
    for i in range(0, lines):
        readMatrixRec(matrix, 0, 2, cols -1)
        for j in range(0, cols):
            print(matrix[i][j], end = " ")
        print()
 
main()
