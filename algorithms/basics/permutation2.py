def func():  
  def printf() -> None:
      for i in range(1, n+1):
          print(stack[i], end = " ")
      print() 
        
  def valid(level) -> bool:
    for i in range(1, level):
        if stack[level] == stack[i]:
          return False
    return True      
        
  def perm(level) -> None:
      if level > n:
         printf()
      else:
         for i in range(1, n+1):
           stack[level] = i
           if valid(level):              
               perm(level+1)
  n = 4
  stack = [0] * (n + 1)
  perm(1)
func()  
