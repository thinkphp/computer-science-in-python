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
