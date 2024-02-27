# permutations => partitions

def perm():
    n = 3
    sol = [0] * (n+1)
    def ok(k):
        for i in range(1, k):
            if sol[i] == sol[k]:
                return 0
        return 1
    def ok(k):
        for i in range(1, k):
            if sol[i] == sol[k]:
                return 0;
        return 1
    def display():
        for i in range(1, n+1):
            print(sol[i], end = " ")
        print()
    def bkt(k):
        if k == n + 1:
            display()
        else:
            for i in range(1,n+1):
                sol[k] = i;
                if ok(k):
                   bkt(k+1)
    bkt(1)
perm()

print("-"*5)

def main():
    n = 3
    sol = [0] * (n+1)
    def ok(k):
        for i in range(1, k):
            if sol[i] == sol[k]:
                return 0
        return 1
    def getMax(k):
        max = sol[1]
        for i in range(2, k):
            if sol[i] > max:
                max = sol[i]
        return max
    def display():
        for i in range(1, n+1):
            print(sol[i], end = " ")
        print()
    def bkt(k):
        if k == n + 1:
            display()
        else:
            for i in range(1,getMax(k)+2):
                sol[k] = i;
                bkt(k+1)
    bkt(1)
main()
