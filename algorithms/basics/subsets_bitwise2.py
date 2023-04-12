def fn4():

    def solve(n):

        k = 2 ** n

        for i in range(1, k):

            for j in range(0,8):

                if (1<<j)&i:

                    print(j+1, end = " ")

            print()

    n = 3
    solve(n)
fn4()
