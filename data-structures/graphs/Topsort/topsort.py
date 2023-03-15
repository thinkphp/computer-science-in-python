def topsort():

    def dfs(node):

        explored[ node ] = True

        for k in range( 1, nodes + 1):

            if explored[ k ] is False and matrix[ node ][ k ] == 1:

                dfs( k )
        sol.append(node)

    def reverse2(list):
            i = 0
            
            j = len(list)-1
            
            while i < j:
                
                list[i],list[j] = list[j], list[i]
                
                i +=1
                
                j -=1

    def reverse(list):
            newList = list[::-1]
            return newList


    file = open("topsort.in", "r")
    
    #grab the number of the nodes and edges
    list = [int(i) for i in file.readline().split(" ")]
    nodes = list[0];
    edges = list[1];

    #define the matrix
    matrix = [[0 for column in range(nodes+1)] for row in range(nodes+1)]
    explored = [False] * (nodes+1)
    sol = []
    for i in range(0, edges):
       line = file.readline().split(" ")
       x = int(line[0])
       y = int(line[1])
       matrix[x][y] = 1
       edges-=1

    for i in range(1, nodes+1):
        if(explored[i] is False):
           dfs(i)

    sol = reverse(sol)
    print(sol)

topsort()
