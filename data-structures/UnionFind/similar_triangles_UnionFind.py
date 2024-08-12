# Haskel = limbaj functional
# c++, java => limbaj orientat obiect, limbaj procedural

# f : Z -> Z
# factorial :: Integer -> Integer
# a = 10.3
# factorial 0 = 1
# factorial n = n * factorial( n - 1)

# factorial 5

class UnionFind:

    def __init__(self, n):

        self.parent = list( range( n ) )
        self.rank = [ 0 ] * n

    #path compression
    def find(self, u):

        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):

        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:

            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u

            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v

            else:
                self.parent[root_v] = root_u
                self.rank[root_u]+=1

    def are_similar( self, u, v ):

           return self.find( u ) == self.find( v )

def read_input():

    n = int(input("Numarul de triunghiuri: "))
    m = int(input("Numarul de relatii: "))

    uf = UnionFind( n )

    print("Introduceti relatiile de asemanare (i, j): ")
    for _ in range( m ):
        u, v = map(int, input().split())
        uf.union(u-1, v-1)

    i, j = map(int, input("Introduceti triunghiurile de verificat (i,j)").split())

    return uf, i-1, j-1


def main():

    uf, i, j = read_input()

    if uf.are_similar(i, j):

       print(f"Triunghiurile {i+1} si {j+1} sunt asemenea.")

    else:

       print(f"Triunghiurile {i+1} si {j+1} nu sunt asemenea.")

main()
