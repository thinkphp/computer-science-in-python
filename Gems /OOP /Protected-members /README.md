# Protected data members

```python
# Defining a class 
class Geek:  
      
    # protected data members  
    _name = "R2J"
    _roll = 1706256
      
    # public member function  
    def displayNameAndRoll(self):  
  
        # accessing protected data members  
        print("Name: ", self._name)  
        print("Roll: ", self._roll)  
  
  
# creating objects of the class          
obj = Geek()  
  
# calling public member  
# functions of the class  
obj.displayNameAndRoll()  
```

```python
# super class  
class Shape:  
      
    # constructor  
    def __init__(self, length, breadth):  
        self._length = length 
        self._breadth = breadth  
          
    # public member function  
    def displaySides(self):  
  
        # accessing protected data members  
        print("Length: ", self._length)  
        print("Breadth: ", self._breadth)  
  
  
# derived class  
class Rectangle(Shape):  
  
    # constructor  
    def __init__(self, length, breadth):  
  
        # Calling the constructor of 
        # Super class 
        Shape.__init__(self, length, breadth)  
          
    # public member function  
    def calculateArea(self):  
                      
        # accessing protected data members of super class  
        print("Area: ", self._length * self._breadth)  
                      
  
# creating objects of the  
# derived class          
obj = Rectangle(80, 50)  
  
# calling derived member  
# functions of the class 
obj.displaySides() 
  
# calling public member 
# functions of the class  
obj.calculateArea()  
```
