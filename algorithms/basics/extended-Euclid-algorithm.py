def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y

# Example usage:
a = 24
b = 15

d, x, y = extended_euclid(a, b)
print("gcd(a, b) =", d)
print("x =", x)
print("y =", y)
