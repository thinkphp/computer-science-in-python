def main():
    # Input : 1
    #         d5
    # output:
    # a5 b5 c5 e5 f5 g5 h5 d1 d2 d3 d4 d6 d7 d8
    def solve():
        rook = input()
        for i in range(97,105):
            if rook[0] != chr(i):
               print(chr(i) + rook[1])
        for j in range(1, 9):
            if str(rook[1]) != str(j):
               print(rook[0] + str(j))
    T = int(input())

    while T != 0:
        solve()
        T-=1

if __name__ == "__main__":

    main()
