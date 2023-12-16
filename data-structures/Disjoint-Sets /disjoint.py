class UnionFind:

    def __init__(self, numElements):
        self.numElements = numElements
        self.parent = [0] * (numElements+1)
        self.height = [0] * (numElements+1)
        for i in range(1, numElements+1):
            self.parent[ i ] = i
            self.height[ i ] = 1

    def union(self, x, y):
        rootX = self.getRoot(x)
        rootY = self.getRoot(y)

        if self.height[ rootX ] > self.height[ rootY ]:
            self.parent[ rootY ] = rootX
        elif self.height[ rootX ] < self.height[ rootY ]:
            self.parent[ rootX ] = rootY
        else:
            self.parent[ rootY ] = rootX
            self.height[ rootX ] += 1

    def getRoot(self, node):

        root = self.parent[ node ]

        while root != self.parent[ root ]:
            root = self.parent[ root ]

        return root

    def find(self, x, y):
        return self.getRoot(x) == self.getRoot(y)

def main():
    file = open("disjoint.in","r")
    #inp = [int(i) for i in input().split()]
    inp = [int(i) for i in file.readline().split()]
    n = inp[0]
    numOps = inp[1]

    uf = UnionFind( n )

    out = open("disjoint.out","w+")
    while numOps:
        #inp = [int(i) for i in input().split()]
        inp = [int(i) for i in file.readline().split()]

        type = inp[0]
        x = inp[1]
        y = inp[2]
        if type == 1:
            uf.union(x,y)
        elif type == 2:
            if uf.find(x, y):
                out.write(str("DA\n"))
                print("DA", end = "\n")
            else:
                out.write(str("NU\n"))
                print("NU", end = "\n")
        numOps-=1
main()
