class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Using the static methods
result1 = MathUtils.add(5, 3)
result2 = MathUtils.multiply(4, 2)

print(result1)  # Output: 8
print(result2)  # Output: 8
