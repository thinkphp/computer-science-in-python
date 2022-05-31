#
# Subsets of a set using Bitwise.
# 0001
# 0010
# 0011
# 0101
#
def pow(x, y):
    p = 1
    for i in range(1, y + 1):
        p *= x
    return p

def generate_subsets( n ):
    for i in range(1, pow(2, n)):
        for j in range(0, n):
            if i&(1<<j):
                print(j + 1, end = " ")
        print()

def main():

    generate_subsets(5)

main()
