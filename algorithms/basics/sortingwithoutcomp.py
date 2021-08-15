def main():
    matrix = [[0 for j in range(0, 100)] for i in range(0, 100)]
    vec = [10,22,31,4,51,62,7,82,83,81,91,90]
    ten = 1
    digits = 3
    N = len(vec)
    print(vec)
    for digit in range(1, digits):
        if digit > 1:
            ten = ten * 10
        for i in range(0, N):
            dig = (vec[ i ] // ten) % 10
            matrix[ 0 ][ dig ] += 1
            matrix[ matrix[0][dig] ][ dig ] = vec[ i ]
 
        k = 0
        for i in range(0, 10):
            if matrix[0][i] != 0:
                for j in range(1, matrix[0][i]+1):
                    vec[k] = matrix[j][i]
                    k += 1
        for i in range(0, 10):
            matrix[0][i] = 0
 
    '''
    for i in range(0, 10):
        for j in range(0, 10):
            print(matrix[i][j], end = " ")
        print("")
    '''
 
    for i in range(0, N):
        print(vec[i], end = " ")
main()
