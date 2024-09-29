import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Finding the block where the element is present (if it is present)
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Doing a linear search for x in the block beginning with prev
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    # If element is found
    if arr[prev] == x:
        return prev

    return -1

# Example usage
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    x = 55

    index = jump_search(arr, x)

    if index != -1:
        print(f"Number {x} is at index {index}")
    else:
        print(f"Number {x} is not in the array.")
