import sys

class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

def compare_edges(a):
    return a.cost

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def unite(self, u, v):
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
    input_file = 'apm.in'
    output_file = 'apm.out'

    with open(input_file, 'r') as infile:
        N, M = map(int, infile.readline().split())
        edges = []

        for _ in range(M):
            u, v, cost = map(int, infile.readline().split())
            edges.append(Edge(u, v, cost))

    edges.sort(key=compare_edges)

    uf = UnionFind(N + 1)  # N + 1 because nodes are 1-indexed
    mst = []
    total_cost = 0

    for edge in edges:
        if uf.find(edge.u) != uf.find(edge.v):
            uf.unite(edge.u, edge.v)
            mst.append(edge)
            total_cost += edge.cost

    with open(output_file, 'w') as outfile:
        outfile.write(f"{total_cost}\n")
        outfile.write(f"{len(mst)}\n")
        for edge in mst:
            outfile.write(f"{edge.u} {edge.v}\n")

if __name__ == "__main__":
    main()
