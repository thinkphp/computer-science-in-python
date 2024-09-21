MAXN = 100001

# Graphs and stack
Graph = [[] for _ in range(MAXN)]
Graph_REVERSE = [[] for _ in range(MAXN)]
Stack = []
isVisited = [False] * MAXN
Results = [[] for _ in range(MAXN)]

# Variables for the number of nodes, edges, and components
nodes = 0
edges = 0
comp = 0

def readData():
    global nodes, edges
    with open("ctc.in", "r") as fin:
        nodes, edges = map(int, fin.readline().split())
        for _ in range(edges):
            x, y = map(int, fin.readline().split())
            Graph[x].append(y)
            Graph_REVERSE[y].append(x)

def DFS(node):
    isVisited[node] = True
    for neighbor in Graph[node]:
        if not isVisited[neighbor]:
            DFS(neighbor)
    Stack.append(node)

def DFS_REVERSE(node):
    isVisited[node] = True
    Results[comp].append(node)
    for neighbor in Graph_REVERSE[node]:
        if not isVisited[neighbor]:
            DFS_REVERSE(neighbor)

def Kosaraju():
    global comp
    # First DFS to populate the stack
    for i in range(1, nodes + 1):
        if not isVisited[i]:
            DFS(i)

    # Reset isVisited for the second DFS pass
    isVisited[:] = [False] * MAXN

    # Second DFS based on the reverse graph and stack order
    while Stack:
        vertex = Stack.pop()
        if not isVisited[vertex]:
            comp += 1
            DFS_REVERSE(vertex)

def writeData():
    with open("ctc.out", "w") as fout:
        fout.write(f"{comp}\n")
        for i in range(1, comp + 1):
            fout.write(" ".join(map(str, Results[i])) + "\n")

def main():
    readData()
    Kosaraju()
    writeData()

if __name__ == "__main__":
    main()
