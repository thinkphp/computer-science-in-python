# Introduction to Functional Programming in Python 3

## What is Functional Programming?

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. Key concepts include:

1. Pure functions
2. Immutability
3. First-class and higher-order functions
4. Recursion

## Key Concepts in Python

### 1. Pure Functions

Pure functions always produce the same output for the same input and have no side effects.

```python
# Pure function
def add(a, b):
    return a + b

# Impure function (uses global state)
total = 0
def impure_add(a):
    global total
    total += a
    return total
```

### 2. Immutability

Favor immutable data structures to prevent unexpected changes.

```python
# Use tuples instead of lists for immutability
immutable_coords = (1, 2, 3)
# Use frozenset instead of set
immutable_set = frozenset([1, 2, 3])
```

### 3. First-Class and Higher-Order Functions

Functions can be assigned to variables, passed as arguments, and returned from other functions.

```python
def apply_operation(func, a, b):
    return func(a, b)

result = apply_operation(add, 3, 4)  # Returns 7
```

### 4. Recursion

Use recursion instead of loops for repetitive tasks.

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
```

## Functional Programming Tools in Python

1. `map()`: Apply a function to all items in an iterable
2. `filter()`: Create a list of elements for which a function returns True
3. `reduce()`: Apply a function of two arguments cumulatively to the items of a sequence
4. Lambda functions: Create small anonymous functions
5. List comprehensions: Create lists based on existing lists

```python
numbers = [1, 2, 3, 4, 5]

# Using map
squared = list(map(lambda x: x**2, numbers))

# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Using reduce
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)

# List comprehension
squared_comp = [x**2 for x in numbers]
```

## Benefits of Functional Programming

1. Easier to reason about and debug
2. Improved code reusability
3. Better support for parallel/concurrent programming
4. Reduced side effects and mutable state

## Conclusion

Functional programming in Python offers a powerful approach to solving problems. While Python is not a purely functional language, it provides many tools to support functional programming paradigms. As Harvard students, understanding these concepts will enhance your programming skills and broaden your approach to problem-solving in computer science.
