import numpy as np
# Крок 1: Метод Сімпсона
def integral_simpson(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    integral_value = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
    return integral_value

# Заміна змінних: x = u^2
def g(u):
    return 2 / (1 + u**4)
def runge_rule(I1, I2, p):
    return (I2 - I1) / (2**p - 1)

# Визначення параметрів інтегралу
a, b = 0, 1  # нові межі інтегралу після заміни змінних
n = 100  # кількість підінтервалів
eps = 0.5  # точність

# Обчислення інтегралу за допомогою методу Сімпсона
I_simpson = integral_simpson(g, a, b, n)

# Перевірка точності: обчислюємо інтеграл з подвоєнням кількості підінтервалів
I_simpson_double_n = integral_simpson(g, a, b, 2*n)

# Оцінка похибки за правилом Рунге (для методу Сімпсона p=4)
error_estimate = runge_rule(I_simpson, I_simpson_double_n, p=4)

I_simpson, I_simpson_double_n, error_estimate, abs(I_simpson - I_simpson_double_n) < eps
