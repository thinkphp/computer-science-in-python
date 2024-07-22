class UnionFind:
    def __init__(self, grid):
        self.parent = {}
        self.rank = {}
        self.count = 0  # numărul de componente disjuncte (insule)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.parent[(i, j)] = (i, j)
                    self.rank[(i, j)] = 0
                    self.count += 1

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            # Unim arborele mai mic sub cel mai mare pentru a minimiza înălțimea
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            self.count -= 1  # Scădem numărul de componente disjuncte

def numIslands(grid):
    if not grid:
        return 0

    uf = UnionFind(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "1":
                        uf.union((i, j), (ni, nj))

    return uf.count

# Exemplu de utilizare
grid = [
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid))  # Output: 3
