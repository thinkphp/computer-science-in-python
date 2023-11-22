## Private variables

```
class Maths:
    
    def __init__(self, n):
        self.n = n
    
    def sign(self,num):
        
        if num > 0:
            print("positive")
        elif num < 0:
            print("negative")
        else:
            print("zero")
            
    def _sqr(self):        
        print(self.n * self.n)
        
    def sqr(self):        
        self._sqr()
    
    def sqrt(self):
        x = self.n
        y = 1
        eps = 0.00001
        while x - y > eps:
            x = (x + y) / 2
            y = self.n/x
        print(x)    
            
            
    def hello(self, name, loud = False):
        
        if loud == True:
            print("HELLO, %s"%name.upper())
        else:
            print("Hello, %s"%name)
            
            
def main():
    ob = Maths(2)
    for i in [-1,0,1]:
        ob.sign(i)
    ob.hello("Adrian",False)    
    ob.sqrt()
    ob.sqr()
    ob._sqr()
main()  
```
