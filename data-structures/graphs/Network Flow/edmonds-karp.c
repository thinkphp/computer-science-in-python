#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>

#define V 6 // Number of vertices
#define INF INT_MAX

int adjMatrix[V][V];
char* vertexNames[V] = {"s", "v1", "v2", "v3", "v4", "t"};

void addEdge(int from, int to, int capacity) {
    adjMatrix[from][to] = capacity;
}

// BFS function to find the shortest path from source to sink
bool bfs(int parent[], int source, int sink) {
    bool visited[V];
    memset(visited, 0, sizeof(visited));
    int queue[V], front = 0, rear = 0;

    queue[rear++] = source;
    visited[source] = true;
    parent[source] = -1;

    while (front < rear) {
        int u = queue[front++];

        for (int v = 0; v < V; v++) {
            if (!visited[v] && adjMatrix[u][v] > 0) {
                if (v == sink) {
                    parent[v] = u;
                    return true;
                }
                queue[rear++] = v;
                parent[v] = u;
                visited[v] = true;
            }
        }
    }
    return false;
}

int edmondsKarp(int source, int sink) {
    int u, v;
    int parent[V]; // Store the path
    int maxFlow = 0;

    while (bfs(parent, source, sink)) {
        int pathFlow = INF;

        // Find the maximum flow through the path found.
        for (v = sink; v != source; v = parent[v]) {
            u = parent[v];
            pathFlow = pathFlow < adjMatrix[u][v] ? pathFlow : adjMatrix[u][v];
        }

        // Update capacities and reverse capacities of the edges and reverse edges
        for (v = sink; v != source; v = parent[v]) {
            u = parent[v];
            adjMatrix[u][v] -= pathFlow;
            adjMatrix[v][u] += pathFlow;
        }

        maxFlow += pathFlow;

        // Code just for printing the path
        int path[V], pathSize = 0;
        for (v = sink; v != -1; v = parent[v]) {
            path[pathSize++] = v;
        }

        printf("Path: ");
        for (int i = pathSize - 1; i >= 0; i--) {
            printf("%s", vertexNames[path[i]]);
            if (i > 0) printf(" -> ");
        }
        printf(", Flow: %d\n", pathFlow);
    }
    return maxFlow;
}

int main() {
    memset(adjMatrix, 0, sizeof(adjMatrix));

    addEdge(0, 1, 3);
    addEdge(0, 2, 7);
    addEdge(1, 3, 3);
    addEdge(1, 4, 4);
    addEdge(2, 1, 5);
    addEdge(2, 4, 3);
    addEdge(3, 4, 3);
    addEdge(3, 5, 2);
    addEdge(4, 5, 6);

    printf("The maximum possible flow is %d\n", edmondsKarp(0, 5));
    return 0;
}

//C
