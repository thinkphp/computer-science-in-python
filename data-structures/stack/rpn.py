class RPN:
    def __init__(self):
        self.stack = []
        self.result = 0
 
    def push(self, data):
        self.stack.append(float(data))
 
    def pop(self):
        return self.stack.pop(len(self.stack)-1)
 
    def operation(self, op):
        term1 = self.pop()
        term2 = self.pop()        
        self.result = eval('%f%c%f'%(term2,op,term1))
        self.push(self.result)
 
    def eval(self,str):
        print("Evaluating",str)
        for ch in str.split(" "):
            if ch in '+-*/':
                self.operation(ch)
            else:
                self.push(ch)
        return self.result
def main():
    c = RPN()
    print(c.eval("1 2 3 4 5 + + + +"))
main()
