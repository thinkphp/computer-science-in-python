def func():

    def ok(level):

        return True

    def print_sol():
        
        max = stack[1]
        
        for i in range(2, n + 1):
            
            if max < stack[i]:
                
               max = stack[i]
               
        for i in range(1, max+1):
            
            print("{", end = " ")
            
            for j in range(1, n + 1):
                
                if i == stack[j]:
                    
                    print(j, end = " ")
                    
            print("}", end = "")
            
        print()    

    def partition(level):
        if level > n:
           print_sol()
        else:
          for i in range(1, n + 1 ):
             if stack[level] < stack[ level - 1 ] + 1:
                stack[level] = i
                if ok(level):
                   partition( level + 1 )
    n = 3
    stack = [0] * (n+1)
    partition(1)

func()
