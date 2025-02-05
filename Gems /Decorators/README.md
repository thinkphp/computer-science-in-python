# Decorators

In Python, decorators are a powerful tool that allows you to modify the behavior of functions without altering their original code. When working with decorators that need to handle functions with a variable number of arguments, you can leverage `*args` and `**kwargs` to achieve flexibility.

**Understanding *args and **kwargs**

* `*args`: This syntax packs any positional arguments passed to the function into a tuple. It allows the function to accept any number of positional arguments.
* `**kwargs`: This syntax packs any keyword arguments passed to the function into a dictionary. It allows the function to accept any number of keyword arguments, named according to the keywords used. 

**Decorators with *args and **kwargs**

Here's how you can create decorators that handle variable arguments:

1. **Decorator Definition:**
   - Define the decorator function using `def`.
   - Within the function, use `*args` and `**kwargs` to capture any positional and keyword arguments passed to the decorator.
   - The decorated function itself will also be passed as an argument (often named `func`).

2. **Wrapper Function:**
   - Inside the decorator, define a wrapper function that will handle the actual logic. 
   - This wrapper function can access the original function (`func`), `args`, and `kwargs`.

3. **Wrapper Function Behavior:**
   - The wrapper function can perform actions before or after calling the original function.
   - It can modify `args` or `kwargs` before passing them on to `func`.

4. **Returning the Wrapper:**
   - Finally, the decorator function returns the wrapper function. 

**Example: Logging Decorator**

Here's an example of a decorator that logs the function call with its arguments:

```python
def log_function(func):
  def wrapper(*args, **kwargs):
    # Log function name and arguments before execution
    print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
    result = func(*args, **kwargs)
    # Log function name and return value after execution (optional)
    # print(f"Function {func.__name__} returned: {result}")
    return result
  return wrapper

@log_function
def add(x, y):
  return x + y

result = add(5, 3)
print(result)  # Output: Calling add with arguments: (5, 3), 8
```

In this example, the `log_function` decorator captures both positional and keyword arguments using `*args` and `**kwargs`. The wrapper function logs the function call information before executing the original `add` function.

**Key Points:**

* By using `*args` and `**kwargs` in decorators, you can create flexible functions that can handle a variable number of arguments.
* The wrapper function within the decorator provides a layer of control to modify behavior before or after the original function execution.

Remember, decorators with `*args` and `**kwargs` offer a powerful way to enhance your functions without modifying their core logic.


### References:

- https://www.geeksforgeeks.org/decorators-in-python/
