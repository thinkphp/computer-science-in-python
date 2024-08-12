from collections import deque

def read_input():

    n = int(input("Numarul de triunghiuri: "))
    m = int(input("Numarul de relatii: "))

    #lista de adiacenta
    graph = [[] for _ in range(n)]
    print(graph)

    print("Introduceti relatiile de asemanare (i,j): ")
    #
    # 1 2 => input.split() ['1','2'] => map(int, input.split()) returneaza [1,2]
    #
    for _ in range(m):

        u, v = map(int, input("(i,j): ").split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    i, j = map(int, input("Introduceti triunghiurile de verificat (i, j): ").split())

    # Introduceti triunghiurile de verificat (i, j)1 5


    return graph, i-1, j-1


def BFS( graph, start ):

    visited = [ False ] * len(graph)

    queue = deque([start])

    visited[ start ] = True

    while queue:

        node = queue.popleft()

        for neighbor in graph[node]:

            if not visited[neighbor]:

                visited[neighbor] = True

                queue.append(neighbor)

    return visited


def are_similar(graph, i, j):

    visited = BFS(graph, i)

    return visited[ j ]

def main():

    graph,i,j=read_input()

    print(graph)

    if are_similar(graph, i, j):

        print(f"Triunghiurile {i+1} si {j+1} sunt asemenea.")
    else:
        print(f"Triunghiurile {i+1} si {j+1} nu sunt asemenea.")

main()
