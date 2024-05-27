# Computer Science in Python

Computer science is no more about computers than astronomy is about telescopes, biology is about microscopes or chemistry is about beakers and test tubes. Science is not about tools, it is about how we use them and what we find out when we do. (Michael Fellows and Ian Parberry, “SIGACT trying to get children excited about CS”)



#### Preface

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

#### Variables

#### Data Types

#### Strings

```python

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# Python code to demonstrate working of 
# strip(), lstrip() and rstrip() 
str = "---python3---"

# using strip() to delete all '-' 
print ( " String after stripping all '-' is : ", end="") 
print ( str.strip('-') ) 

# using lstrip() to delete all trailing '-' 
print ( " String before stripping all leading '-' is : ", end="") 
print ( str.lstrip('-') ) 

# using rstrip() to delete all leading '-' 
print ( " String after stripping all trailing '-' is : ", end="") 
print ( str.rstrip('-') ) 
```

#### Numbers

#### Boolean

#### Exception handling

#### Data Members

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

#### Programming Contests

Experimental Educational Round: VolBIT Formulas Blitz https://codeforces.com/contest/630

VK Cup 2015 - Wild Card Round 1 https://codeforces.com/contest/530

Codeforces Alpha Round 20 https://codeforces.com/contest/20 (A. BerOS file system1, B. Equation, C. Dijkstra?)

Codeforces Round 948 (Div. 2) https://codeforces.com/contest/1977

Codeforces Beta Round 82 (Div. 2) https://codeforces.com/contest/106

Codeforces Round 907 (Div. 2) https://codeforces.com/contest/1891

Codeforces Round 134 (Div. 2) https://codeforces.com/contest/218

Codeforces Round 587 (Div. 3) https://codeforces.com/contest/1216

Codeforces Round 486 (Div. 3) https://codeforces.com/contest/988

Codeforces Round 479 (Div. 3) https://codeforces.com/contest/977

Codeforces Round 481 (Div. 3) https://codeforces.com/contest/978

Codeforces Round 928 (Div. 4) https://codeforces.com/contest/1926

Codeforces Round 640 (Div. 4) https://codeforces.com/contest/1352

Codeforces Round 784 (Div. 4) https://codeforces.com/contest/1669

### EDU Codeforces
https://codeforces.com/edu/courses

### References

https://www.amazon.com/Introduction-Algorithms-Thomas-H-Cormen/dp/0262033844/

https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/?ref=shm

https://web.stanford.edu/class/cs97si/

https://www.enjoyalgorithms.com/

https://www.programming-books.io/essential/python/

https://mcsp.wartburg.edu/zelle/python/

https://www.cfm.brown.edu/people/dobrush/am33/python/index.html

https://github.com/rtoal/ple/tree/main/python


#### My Favourite Books:

An Introduction to Programming in Python. An interdisciplinary Approach. Robert Sedgwick.

A Beginners Guide To Python 3 Programming - Springer

Advanced Guide To Python 3 Programming - Springer 

Python for Probability, Statistics, and Machine Learning - Springer

