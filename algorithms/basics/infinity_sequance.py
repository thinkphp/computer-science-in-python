def infinite_sequence():    
    num = 0
    while True:
        if num % 2 != 0:
           yield num        
        num+=1
def fn():    
    n = int(input())
    gen = infinite_sequence()
    p = 1
    for i in range(1,n+1):
        
        p = p * next(gen)
    print(p)    
      
fn()
