def main():
    def isPrime(n):
        if n <= 1: return False
        if n == 2 or n == 3: return True
        prime = True
        i = 2
        while i * i <= n and prime is True:
            prime = (n % i) != 0
            i += 1
        return prime

    n = int(input("n="))
    m = int(input("m="))
    matrix = [[0 for j in range(0,m)] for i in range(0,n+1)]
    for i in range(0,n):
        for j in range(0,m):
            matrix[i][j] = int(input("elem="))
    for i in range(0,n):
        for j in range(0,m):
            print(matrix[i][j], end=" ")
        print()

    for i in range(0, n):
        for j in range(0,m):
            if not(matrix[i][j]&1):
               print("matrix[%d][%d] = %d"%(i,j,matrix[i][j]), end ="\n")
               for k in range(2, matrix[i][j]//2+1):
                   if isPrime(k) is True and isPrime(matrix[i][j]-k) is True:
                       print("%d = %d + %d "%(matrix[i][j], k, matrix[i][j] - k), end="\n")

main()
