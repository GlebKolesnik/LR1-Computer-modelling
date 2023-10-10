import numpy as np

def runge_rule(I1, I2, p):
    return (I2 - I1) / (2**p - 1)

def integral_left_rectangles(func, a, b, n):
    h = (b - a) / n
    integral_value = 0
    for i in range(n):
        integral_value += func(a + i*h)
    integral_value *= h
    return integral_value

def h(t):
    x = 2/(1 - t)
    return 2/((1 - t)**2 * (1 + x**3))

a, b = 0, 1
n = 1000
eps = 0.005

I_left = integral_left_rectangles(h, a, b, n)
I_left_double_n = integral_left_rectangles(h, a, b, 2*n)
error_estimate = runge_rule(I_left, I_left_double_n, p=1)

print("I (n intervals) =", I_left)
print("I (2n intervals) =", I_left_double_n)
print("Estimated error =", error_estimate)
print("Is the actual error less than eps? :", abs(I_left - I_left_double_n) < eps)
