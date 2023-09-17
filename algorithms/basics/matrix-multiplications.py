import random
class Matrix:
    def __init__(self,n,m,opt=0):
        self.n = n;
        self.m = m;
        if opt == 0:
           self.matrix = [[random.randint(2,10) for j in range(m+1)] for i in range(n+1)]
        else:
           self.matrix = [[0 for j in range(m+1)] for i in range(n+1)]

    def __repr__(self):
        mat = ""
        for i in range(self.n):
            for j in range(self.m):
                mat += str(self.matrix[i][j]) + " "
            mat += "\n"
        return mat

def product(mat1, mat2)->Matrix:
    prod = Matrix(3,3,1)
    for i in range(0,mat1.n):
        for j in range(0, mat2.m):
            for k in range(0, mat2.m):
                prod.matrix[i][j] += mat1.matrix[i][k] * mat2.matrix[k][j]
    return prod

def fn():
    mat1 = Matrix(3,3)
    mat2 = Matrix(3,3)
    print("Matrix 1:")
    print(mat1)
    print("Matrix 2:")
    print(mat2)
    prod = product(mat1, mat2)
    print("Matrix Multiplication:")
    print(prod)
fn()
