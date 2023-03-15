def dfs(matrix, nodes, startNode):

    stack = [0] * (nodes+1)
    
    ptr = 0
    
    explored = [0] * (nodes+1)
    
    explored[startNode] = 1
    
    stack[ptr] = startNode
    
    print(startNode+1, end = " ")
    
    while ptr>=0:
    
        node = stack[ptr]
        
        found = 0
        
        k = 0
        
        while k < nodes and found == 0:
        
            if matrix[node][k] == 1 and explored[k] == 0:
            
                found = 1
            k+=1
            
        if found == 0:
        
            ptr-=1
            
        else:
        
            print(k, end = " ")
            
            explored[k-1] = 1
            
            ptr+=1
            
            stack[ptr] = k -1


def func():

    file = open("graph.in","r")

    nodes = int(file.readline())

    matrix = [[int(num) for num in line.split(' ')] for line in file]

    startNode = 0

    dfs(matrix, nodes, startNode)

func()
