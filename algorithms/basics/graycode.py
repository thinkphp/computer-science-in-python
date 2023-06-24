"""
A Gray code is a list of all 2n
 bit strings of length n, 
 where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).
 
Your task is to create a Gray code for a given length n.
 
Input:
2
 
Output:
00
01
11
10
"""
 
def makeBinary(n, total):
    res = ["0" for _ in range(total)]
    i = total - 1
    while n > 0:
        aux = n % 2
        if aux:
            res[i] = "1"
        else:
            res[i] = "0"
        n //= 2
        i -= 1
    print("".join(res))
 
 
def generateGreyCode() -> None:
    n = int(input())
    for i in range(0, 1<<n):
        gray = i^(i>>1)
        makeBinary(gray, n)
 
generateGreyCode()
