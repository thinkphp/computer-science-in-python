def fibonacci_search(arr, x):
    # Initialize Fibonacci numbers
    fib2 = 0  # (m-2)'th Fibonacci number
    fib1 = 1  # (m-1)'th Fibonacci number
    fib = fib1 + fib2  # m'th Fibonacci number

    # Find the smallest Fibonacci number greater than or equal to len(arr)
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    # Initialize the offset
    offset = -1

    while fib > 1:
        # Check if fib2 is a valid index
        i = min(offset + fib2, len(arr) - 1)

        # If x is greater than the value at index i, cut the subarray from offset to i
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        # If x is less than the value at index i, cut the subarray after i+1
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        # Element found
        else:
            return i

    # Compare last element with x
    if fib1 and arr[offset + 1] == x:
        return offset + 1

    # Element not found
    return -1

# Example usage and tests
if __name__ == "__main__":
    # Example 1: Basic search
    arr1 = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    x1 = 85
    result1 = fibonacci_search(arr1, x1)
    print(f"Example 1: Searching for {x1} in {arr1}")
    print(f"Result: {'Found at index ' + str(result1) if result1 != -1 else 'Not found'}\n")

    # Example 2: Element not in the array
    arr2 = [1, 3, 5, 7, 9, 11, 13, 15]
    x2 = 8
    result2 = fibonacci_search(arr2, x2)
    print(f"Example 2: Searching for {x2} in {arr2}")
    print(f"Result: {'Found at index ' + str(result2) if result2 != -1 else 'Not found'}\n")

    # Example 3: Element at the beginning
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x3 = 1
    result3 = fibonacci_search(arr3, x3)
    print(f"Example 3: Searching for {x3} in {arr3}")
    print(f"Result: {'Found at index ' + str(result3) if result3 != -1 else 'Not found'}\n")

    # Example 4: Element at the end
    arr4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    x4 = 100
    result4 = fibonacci_search(arr4, x4)
    print(f"Example 4: Searching for {x4} in {arr4}")
    print(f"Result: {'Found at index ' + str(result4) if result4 != -1 else 'Not found'}\n")

    # Example 5: Empty array
    arr5 = []
    x5 = 5
    result5 = fibonacci_search(arr5, x5)
    print(f"Example 5: Searching for {x5} in {arr5}")
    print(f"Result: {'Found at index ' + str(result5) if result5 != -1 else 'Not found'}")
