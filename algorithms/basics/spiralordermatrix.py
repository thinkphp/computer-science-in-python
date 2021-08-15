import random
 
def main():
    N = 5
    matrix = [[0 for j in range(0, 100)] for i in range(0, 100)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            matrix[i][j] = random.randint(1,9)
 
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(matrix[i][j], end = " ")
        print()
 
 
 
    print("Spiral Order Matrix ->")
 
    for k in range(1, N // 2 + 1 + 1):
 
        for i in range(k, N - k + 1 + 1):
            print(matrix[ k ][ i ], end = " ")
 
        for i in range(k + 1, N - k + 1 + 1):
            print(matrix[ i ][ N - k + 1 ], end = " ")
 
        for i in range(N - k, k - 1,-1):
            print(matrix[ N - k  + 1 ][ i ], end = " ")
 
        for i in range(N - k, k,-1):
            print(matrix[ i ][ k ], end = " ")
 
 
    print("")
main()
 
