class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

def compare_edges( a ):
       return a.cost

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
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
                self.rank[root_u] += 1

def main():

    input_file = "apm.in"
    output_file = "apm.out"
    #ifstream fin("apm.in") in c++
    with open(input_file, "r") as inFile:
        N, M = map( int, inFile.readline().split() )
        #print(N, M)
        edges = []
        for _ in range(M):
            u, v, cost = map(int, inFile.readline().split())
            edges.append(Edge(u, v, cost))

        #sortam muchiile dupa cost in ordine ascendenta

        for edge in edges:
            print(f" [ {edge.u}, {edge.v} ] si cost = {edge.cost}")

        edges.sort( key = compare_edges )

        print("Muchiile sortate dupa COST:")

        for edge in edges:
            print(f" [ {edge.u}, {edge.v} ] si cost = {edge.cost}")

        uf = UnionFind(N+1)

        MinimumSpanningTree = []

        total_cost = 0

        for edge in edges:

            if uf.find(edge.u) != uf.find(edge.v):

                uf.union(edge.u, edge.v)

                MinimumSpanningTree.append(edge)

                total_cost += edge.cost

        with open(output_file, "w") as outFile:

            outFile.write(f"{total_cost}\n")

            outFile.write(f"{len(MinimumSpanningTree)}\n")

            for edge in MinimumSpanningTree:

                outFile.write(f"{edge.v} {edge.u} \n")

main()
