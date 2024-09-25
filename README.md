# Computer Science in Python

# Example 1: Importing a module
import math
print(math.sqrt(16))

# Example 2: Importing specific functions
from math import pi, pow
print(pi, pow(2, 3))

# Example 3: Custom module (if students create their own)
import my_module  # Assuming there's a my_module.py file





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
### Programming Contests

#### Educational Codeforces 

Round  1 https://codeforces.com/contest/598

Round 26 https://codeforces.com/contest/837

Experimental Educational Round: VolBIT Formulas Blitz https://codeforces.com/contest/630

VK Cup 2015 - Wild Card Round 1 https://codeforces.com/contest/530

Codeforces Alpha Round 20 https://codeforces.com/contest/20 (A. BerOS file system1, B. Equation, C. Dijkstra?)

April Fools Day Contest 2024 https://codeforces.com/contest/1952

#### Div. 1

Codeforces Round 808 (Div. 1) https://codeforces.com/contest/1707

#### Div. 2

Codeforces Round 213 (Div. 2) https://codeforces.com/contest/365

Codeforces Round 934 (Div. 2) https://codeforces.com/contest/1944

Codeforces Round 726 (Div. 2) https://codeforces.com/contest/1537

Codeforces Round 926 (Div. 2) https://codeforces.com/contest/1929

Codeforces Beta Round 9 (Div. 2) https://codeforces.com/contest/9

Educational Codeforces Round 161 (Div. 2) https://codeforces.com/contest/1922

Codeforces Beta Round 91 (Div. 2) https://codeforces.com/contest/122

Codeforces Round 948 (Div. 2) https://codeforces.com/contest/1977

Codeforces Beta Round 82 (Div. 2) https://codeforces.com/contest/106

Codeforces Round 907 (Div. 2) https://codeforces.com/contest/1891

Codeforces Round 134 (Div. 2) https://codeforces.com/contest/218

#### Div.3 
Codeforces Round 946 (Div. 3) https://codeforces.com/contest/1974

Codeforces Round 920 (Div. 3) https://codeforces.com/contest/1921

Codeforces Round 587 (Div. 3) https://codeforces.com/contest/1216

Codeforces Round 486 (Div. 3) https://codeforces.com/contest/988

Codeforces Round 479 (Div. 3) https://codeforces.com/contest/977

Codeforces Round 481 (Div. 3) https://codeforces.com/contest/978

Codeforces Round 929 (Div. 3) https://codeforces.com/contest/1933

Codeforces Round 923 (Div. 3) https://codeforces.com/contest/1927

Codeforces Round 535 (Div. 3) https://codeforces.com/contest/1108

Codeforces Round 529 (Div. 3) https://codeforces.com/contest/1095

#### Div. 4

Codeforces Round 799 (Div. 4) https://codeforces.com/contest/1692

Codeforces Round 928 (Div. 4) https://codeforces.com/contest/1926

Codeforces Round 640 (Div. 4) https://codeforces.com/contest/1352

Codeforces Round 784 (Div. 4) https://codeforces.com/contest/1669

Codeforces Round 835 (Div. 4) https://codeforces.com/contest/1760

Codeforces Round 849 (Div. 4) https://codeforces.com/contest/1791

Codeforces Round 859 (Div. 4) https://codeforces.com/contest/1807

Codeforces Round 827 (Div. 4) https://codeforces.com/contest/1742

Codeforces Round 817 (Div. 4) https://codeforces.com/contest/1722

Codeforces Round 790 (Div. 4) https://codeforces.com/contest/1676

Codeforces Round 898 (Div. 4) https://codeforces.com/contest/1873


####  Happy New Year

Good Bye 2014 https://codeforces.com/contest/500 Editorial: https://codeforces.com/blog/entry/15513

Good Bye 2015 https://codeforces.com/contest/611 Editorial: https://codeforces.com/blog/entry/22441

Good Bye 2016 https://codeforces.com/contest/611 Editorial: https://codeforces.com/blog/entry/49412

Good Bye 2017 https://codeforces.com/contest/908 Editorial: https://codeforces.com/blog/entry/56713 https://codeforces.com/blog/entry/56848

Good Bye 2018 https://codeforces.com/contest/1091 Editorial: https://codeforces.com/blog/entry/64196

Good Bye 2019 https://codeforces.com/contest/1270 Editorial: https://codeforces.com/blog/entry/72611
                                                  
Good Bye 2020 https://codeforces.com/contest/1466 Editorial: https://codeforces.com/blog/entry/86126

Good Bye 2021 https://codeforces.com/contest/1616  Editorial: https://codeforces.com/blog/entry/98501

Good Bye 2022 https://codeforces.com/contest/1770 Editorial: https://codeforces.com/blog/entry/110754

Good Bye 2023 https://codeforces.com/contest/1916 Editorial: https://codeforces.com/blog/entry/124138 

### EDU Codeforces
https://codeforces.com/edu/courses


### Baltic Olympiad in Informatics 2020
Day 1: https://codeforces.com/contest/1386

Day 2: https://codeforces.com/contest/1387

### AtCoder
https://atcoder.jp/contests/abc272/tasks

https://atcoder.jp/contests/abc356/tasks

https://atcoder.jp/contests/abc354/tasks

https://atcoder.jp/contests/abc349/tasks

https://atcoder.jp/contests/abc224/tasks




### Math:

* https://brilliant.org/wiki/bezouts-identity/
* https://www.intmath.com/quadratic-equations/sum-product-roots-quadratic-equation.php
* https://codeforces.com/blog/entry/97623
* https://www.cuemath.com/algebra/nature-of-roots/#What-Do-You-Mean-By-Nature-of-Roots
* https://www.cuemath.com/geometry/x-intercept/
* https://brilliant.org/wiki/vietas-formula/#vietas-formula-problem-solving-easy
* https://artofproblemsolving.com/wiki/index.php/Euclidean_algorithm
* https://artofproblemsolving.com/wiki/index.php/Goldbach_Conjecture
* https://artofproblemsolving.com/wiki/index.php/Math_books

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

