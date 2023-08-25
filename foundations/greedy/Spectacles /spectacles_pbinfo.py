def fn():
    file = open("spectacole.in","r")
    n = int(next(file))
    matrix = []
    for line in file:
        matrix.append([int(x) for x in line.split()])
    print(matrix)
    matrix = sorted(matrix, key = lambda x: x[1])
    curr = matrix[0][1]
    count = 1
    for i in range(1, n):
        if matrix[i][0]>=curr:
           curr = matrix[i][1]
           count+=1
    with open("spectacole.out","w") as file:
         file.write(str(count))
         file.close()
fn()
