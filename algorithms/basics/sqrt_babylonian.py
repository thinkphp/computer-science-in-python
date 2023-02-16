#
# filename:
#    @sqrt_babylonian.py
# Description:
#    @This algorithm computes the sqrt of a number based on Babylonian method
# Created:
#    @Adrian
#
def sqrt_babylonian(num):
    x = num
    y = 1.0
    EPS = 0.000001
    while x - y > EPS:
        x = (x + y) / 2
        y = num / x
    return x

def func():
    num = int(input("num = "))
    res = sqrt_babylonian(num)
    print("sqrt(%d) = %f"%(num,res))
func()
