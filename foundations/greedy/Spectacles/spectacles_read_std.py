def fn():
    n = int(input())
    matrix = []
    for i in range(1,n+1):
        line = input().split(" ")
        a, b = int(line[0]), int(line[1])
        matrix.append([a,b])
    print(matrix)
    matrix = sorted(matrix, key = lambda x: x[1])
    curr = matrix[0][1]
    count = 1
    for i in range(1, n):
        if matrix[i][0]>=curr:
           curr = matrix[i][1]
           count+=1
    print(count)
fn()
