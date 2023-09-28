def sqr(x):
    return x*x
def sqrt(n):
    x = n
    y = 1.0
    eps = 0.000001
    while x - y > eps:
        x = (x + y) / 2
        y = n / x
    return x
def main():
    print("Circle:")
    x0 = float(input("x0="))
    y0 = float(input("y0="))
    R = float(input("R="))
    print("Point:")
    x = float(input("x="))
    y = float(input("y="))
    dist = sqrt(sqr(x-x0) + sqr(y-y0))
    print(dist)
    dist -= R;
    if dist < 0:
        print("The point is inside Circle")
    elif dist == 0:
        print("The point on the Circle")
    else:
        print("The point is outside Circle")

main()
