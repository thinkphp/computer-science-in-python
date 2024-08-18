from collections import deque

def read_input():
    n = int(input("Numărul de noduri: "))
    m = int(input("Numărul de relații: "))
    
    graph = [[] for _ in range(n)]
    
    print("Introduceți relațiile (i, j):")
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    return graph

def bfs(graph, start_node, visited):
    queue = deque([start_node])
    visited[start_node] = True
    component = []
    
    while queue:
        node = queue.popleft()
        component.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return component

def find_connected_components(graph):
    visited = [False] * len(graph)
    components = []
    
    for i in range(len(graph)):
        if not visited[i]:
            component = bfs(graph, i, visited)
            components.append(component)
    
    return components

def main():
    graph = read_input()
    
    components = find_connected_components(graph)
    
    print("Componentele conexe sunt:")
    for component in components:
        print(" ".join(str(node + 1) for node in component))  # Afișăm nodurile 1-based

if __name__ == "__main__":
    main()