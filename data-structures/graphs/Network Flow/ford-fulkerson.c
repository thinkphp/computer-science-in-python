#include <stdio.h>
#include <string.h>
#include <limits.h>

#define V 6 // Total vertices

// Graph structure to hold the adjacency matrix and vertex names
typedef struct {
    int adjMatrix[V][V];
    char* vertexNames[V];
} Graph;

// Initialize the graph with vertex names and zero capacities
void initGraph(Graph* g, char* names[]) {
    memset(g->adjMatrix, 0, sizeof(g->adjMatrix));
    for (int i = 0; i < V; i++) {
        g->vertexNames[i] = names[i];
    }
}

// Add edge to the graph
void addEdge(Graph* g, int from, int to, int cap) {
    g->adjMatrix[from][to] = cap;
}

// Depth-First Search (DFS) for finding an augmenting path
int dfs(Graph* g, int s, int t, int parent[]) {
    static int visited[V]; // Static array to keep track of visited vertices
    memset(visited, 0, sizeof(visited));
    
    // Inner DFS function to recursively search for path
    int dfsVisit(int u) {
        visited[u] = 1;
        if (u == t) return 1; // Sink reached
        
        for (int v = 0; v < V; v++) {
            if (!visited[v] && g->adjMatrix[u][v] > 0) {
                parent[v] = u;
                if (dfsVisit(v)) return 1; // Path found
            }
        }
        return 0;
    }
    
    return dfsVisit(s);
}

// Ford-Fulkerson algorithm for finding maximum flow
int fordFulkerson(Graph* g, int source, int sink) {
    int u, v, max_flow = 0, parent[V];
    
    while (dfs(g, source, sink, parent)) {
        int path_flow = INT_MAX;
        
        // Find minimum capacity in the found path
        for (v = sink; v != source; v = parent[v]) {
            u = parent[v];
            path_flow = path_flow < g->adjMatrix[u][v] ? path_flow : g->adjMatrix[u][v];
        }
        
        // Update capacities and reverse edges along the path
        for (v = sink; v != source; v = parent[v]) {
            u = parent[v];
            g->adjMatrix[u][v] -= path_flow;
            g->adjMatrix[v][u] += path_flow;
        }
        
        max_flow += path_flow;
        
        // Print the path from source to sink
        printf("Path: ");
        int path[V], pathSize = 0;
        for (v = sink; v != source; v = parent[v]) {
            path[pathSize++] = v;
        }
        
        for (int i = pathSize - 1; i >= 0; i--) {
            printf("%s", g->vertexNames[path[i]]);
            if (i > 0) printf(" -> ");
        }
        printf(", Flow: %d\n", path_flow);
    }
    
    return max_flow;
}

int main() {
    Graph g;
    char* vertexNames[] = {"s", "v1", "v2", "v3", "v4", "t"};
    initGraph(&g, vertexNames);
    
    // Adding edges with capacities
    addEdge(&g, 0, 1, 3);
    addEdge(&g, 0, 2, 7);
    addEdge(&g, 1, 3, 3);
    addEdge(&g, 1, 4, 4);
    addEdge(&g, 2, 1, 5);
    addEdge(&g, 2, 4, 3);
    addEdge(&g, 3, 4, 3);
    addEdge(&g, 3, 5, 2);
    addEdge(&g, 4, 5, 6);
    
    printf("The maximum possible flow is %d\n", fordFulkerson(&g, 0, 5));
    return 0;
}

//C
