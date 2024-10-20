#include <iostream>
#include <vector>
#include <limits>
#include <iomanip>

const int INF = std::numeric_limits<int>::max();

class Graph {
private:
    int V; // Number of vertices
    std::vector<std::vector<int>> dist;

public:
    Graph(int vertices) : V(vertices) {
        dist.resize(V, std::vector<int>(V, INF));
        for (int i = 0; i < V; ++i) {
            dist[i][i] = 0;
        }
    }

    void addEdge(int u, int v, int weight) {
        dist[u][v] = weight;
    }

    void royFloyd() {
        for (int k = 0; k < V; ++k) {
            for (int i = 0; i < V; ++i) {
                for (int j = 0; j < V; ++j) {
                    if (dist[i][k] != INF && dist[k][j] != INF &&
                        dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }

    void printDistances() {
        std::cout << "Shortest distances between every pair of vertices:\n";
        for (int i = 0; i < V; ++i) {
            for (int j = 0; j < V; ++j) {
                if (dist[i][j] == INF) {
                    std::cout << std::setw(5) << "INF";
                } else {
                    std::cout << std::setw(5) << dist[i][j];
                }
            }
            std::cout << '\n';
        }
    }
};

int main() {
    Graph g(4);

    g.addEdge(0, 1, 5);
    g.addEdge(0, 3, 10);
    g.addEdge(1, 2, 3);
    g.addEdge(2, 3, 1);

    g.royFloyd();
    g.printDistances();

    return 0;
}
