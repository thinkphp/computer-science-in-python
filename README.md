# Computer Science in Python

### Preface

Python functions are defined using def keywords:

```python
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print sign(x)
# Prints "negative", "zero", "positive"

def hello(name, loud=False):
    if loud:
        print 'HELLO, %s!' % name.upper()
    else:
        print 'Hello, %s' % name

hello('Bob') # Prints "Hello, Bob"
hello('Fred', loud=True)  # Prints "HELLO, FRED!"
```

## Variables

## Data Types

## Strings

## Numbers

## Exception handling


### Data Members

```python
class Person:
  # data members
  salary = 23 
  def __init__(self, name, age):
    Person.name = name
    self.age = age
    Person.salary += 1

  def __str__(self):
    return f"{self.name}({self.age})" + str(Person.salary)    

p1 = Person("John", 36)

print(p1)

```

### Class

We can easily create the classes using class keyword in the following manner:

```python
class Greeter(object):
    
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable
        
    # Instance method
    def greet(self, loud=False):
        if loud:
            print 'HELLO, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name
        
g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"
```

### References

https://www.amazon.com/Introduction-Algorithms-Thomas-H-Cormen/dp/0262033844/

https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/?ref=shm

https://web.stanford.edu/class/cs97si/

https://www.enjoyalgorithms.com/

https://www.programming-books.io/essential/python/

https://mcsp.wartburg.edu/zelle/python/

https://www.cfm.brown.edu/people/dobrush/am33/python/index.html


# My Favourite Books:

A Beginners Guide To Python 3 Programming - Springer

Advanced Guide To Python 3 Programming - Springer 

Python for Probability, Statistics, and Machine Learning - Springer


## Contests Gym Warmup ProblemSet

VK Cup 2015 - Wild Card Round 1 https://codeforces.com/contest/530

Codeforces Alpha Round 20 https://codeforces.com/contest/20
