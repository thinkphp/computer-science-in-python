def fn():
    n = 10
    matrix = [[5, 14], [14, 17], [8, 13], [13, 15], [15, 17], [3, 6], [4, 7], [6, 9], [11, 14], [10, 11]]
    print(matrix)
    matrix = sorted(matrix, key = lambda x: x[1])
    curr = matrix[0][1]
    count = 1
    for i in range(1, n):
        if matrix[i][0]>=curr:
           curr = matrix[i][1]
           count+=1
    print("Count =", count)
fn()
