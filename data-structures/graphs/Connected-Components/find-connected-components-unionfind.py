class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def read_input():
    n = int(input("Numărul de noduri: "))
    m = int(input("Numărul de muchii: "))
    edges = []
    print("Introduceți muchiile (i, j):")
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))  # Convertim la indexare 0-based
    return n, edges


def find_connected_components(n, edges):
    uf = UnionFind(n)

    # Unite nodurile pe baza muchiilor
    for u, v in edges:
        uf.union(u, v)

    # Grupăm nodurile după reprezentant
    components = {}
    for i in range(n):
        root = uf.find(i)
        if root in components:
            components[root].append(i)
        else:
            components[root] = [i]

    # Convertim componentele la o listă de liste
    return list(components.values())


def main():
    n, edges = read_input()
    components = find_connected_components(n, edges)

    print("Componentele conexe sunt:")
    for component in components:
        print(" ".join(str(node + 1) for node in component))  # Afișăm nodurile 1-based


if __name__ == "__main__":
    main()
