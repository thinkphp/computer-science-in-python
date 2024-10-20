1. Graph Class:
   - Represents the graph using an adjacency matrix (`dist`).
   - `V` stores the number of vertices.
   - `INF` represents infinity (unreachable vertices).

2. Constructor:
   - Initializes the distance matrix with `INF`.
   - Sets the distance from a vertex to itself as 0.

3. `addEdge` function:
   - Adds an edge to the graph with a given weight.

4. `royFloyd` function:
   - Implements the Roy-Floyd algorithm.
   - Uses three nested loops to consider all possible intermediate vertices.
   - Updates the distance if a shorter path is found through an intermediate vertex.

5. `printDistances` function:
   - Prints the final distance matrix.

6. Main function:
   - Creates a graph with 4 vertices.
   - Adds edges to the graph.
   - Runs the Roy-Floyd algorithm.
   - Prints the resulting distances.

Key points about the Roy-Floyd algorithm:

1. Time Complexity: O(V^3), where V is the number of vertices.
2. Space Complexity: O(V^2) for the distance matrix.
3. It works with both positive and negative edge weights.
4. It can detect negative cycles if the diagonal of the result matrix contains negative values.

This implementation allows you to easily create a graph, run the Roy-Floyd algorithm, and view the shortest distances between all pairs of vertices. You can modify the `main` function to test different graph configurations.

To use this for larger graphs or read input from a file, you could extend the `main` function to:
1. Read the number of vertices and edges from input.
2. Read each edge and its weight.
3. Construct the graph based on this input.

Would you like to see an example of how to modify this code to handle input for larger graphs, or do you have any questions about the implementation?
