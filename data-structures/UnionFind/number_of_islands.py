class UnionFind:
    def __init__(self, m, n):  # Pass grid dimensions
        self.parent = {i * n + j: i * n + j for i in range(m) for j in range(n)}  # Initialize parent for all cells
        self.size = {i * n + j: 1 for i in range(m) for j in range(n)}  # Initialize size for all cells

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            if self.size[parent1] < self.size[parent2]:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]
            else:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]

def num_islands(grid):
    m, n = len(grid), len(grid[0])
    uf = UnionFind(m, n)  # Pass grid dimensions

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                cell_id = i * n + j

                # Check horizontal and vertical neighbors (if they exist)
                if i > 0 and grid[i - 1][j] == '1':
                    uf.union(cell_id, (i - 1) * n + j)
                if j > 0 and grid[i][j - 1] == '1':
                    uf.union(cell_id, i * n + j - 1)

                # Check right and lower neighbors (if valid)
                if i < m - 1 and grid[i + 1][j] == '1':
                    uf.union(cell_id, (i + 1) * n + j)
                if j < n - 1 and grid[i][j + 1] == '1':
                    uf.union(cell_id, i * n + j + 1)

    # Count the number of islands (root sets) for cells initially marked as '1'
    root_set = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                root_set.add(uf.find(i * n + j))
    return len(root_set)

grid = [
    ['1', '1', '1', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '1', '1'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

num_islands_count = num_islands(grid)
print("Number of islands:", num_islands_count)  # Output: 3
