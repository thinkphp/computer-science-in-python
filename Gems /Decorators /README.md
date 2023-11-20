## Decorators Design Pattern

The idea behind the decorators design pattern in Python is to allow you to modify the functionality of a function or a class by wrapping it in another function or a class. This way, you can add new features or behaviors to existing objects without changing their original code. For example, you can use a decorator to add logging, caching, validation, or timing features to a function or a class.

A decorator in Python is a function or a class that takes another function or a class as an argument and returns a modified version of it. The modified version usually contains some additional code that executes before or after the original function or class. You can apply a decorator to a function or a class by using the @ symbol before its definition. For example, you can define a simple decorator that prints a message before and after calling a function:

```python
def my_decorator(func):
     def wrapper():
         print("Before calling the function")
         func()
         print("After calling the function")
     return wrapper # return the wrapper function
 
@my_decorator # apply the decorator to the function
def say_hello(): # define the original function
     print("Python for Machine Learning!") # print a message
say_hello() # call the decorated function
```

## Examples

https://ideone.com/Aqg875

https://ideone.com/T7POPh
