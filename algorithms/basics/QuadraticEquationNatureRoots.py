def sqrt(n):
    x = n
    y = 1.0
    eps = 0.00001
    while x - y > eps:
        x = (x + y) / 2
        y = n / x
    return x
# Viete's rules = Relatiile lui Viete
# ax^2 + bx + c = 0; a != 0
# x^2 - Sx + P = 0
# S = x1 + x2
# P = x1 * x2
# S = -b/a; P = c/a
# the study of the sign roots of a Quadratic Equation
def Nature_Roots_Quadratic_Equation(a, b, c):
    d = b ** 2 - 4 * a * c
    #a!=0
    S = -b/a
    P = c/a

    print(f"Sum = {S}, Prod = {P}")
    print("Sum = %.2f Prod = %.2f"%(S, P))
    if d < 0:
        return ["imaginary"]
    elif d >= 0:
         x1 = ( -b - sqrt(d) )/ (2*a)
         x2 = ( -b + sqrt(d) ) / (2*a)
         print(f"x1={x1:.2f} x2={x2:.2f}")
         if S > 0:
             if P > 0:
                 return ["x1>0","x2>0"]
             elif P < 0:
                 return ["x1<0","x2>0","|x1|<|x2|"]
                 #x1=-3, x2=7
             else:
                 return ["x1=0","x2>0"]
         # S < 0
         else:
             if P > 0:
                 return ["x1<0","x2<0"]
             elif P < 0:
                 return ["x1<0","x2>0","|x1|>|x2|"]
             else:
                 return ["x1=0","x2<0"]
def main():

    lesson = dict(title = "Viete's Rules", content ="\nNature Roots Quadratic Equation")

    print("Today we'll learn about:\n{title} {content}".format(**lesson))

    A = 1
    B = 5
    C = 2
    print(*Nature_Roots_Quadratic_Equation(A,B,C), sep="\n")

main()
