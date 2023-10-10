import numpy as np
import matplotlib.pyplot as plt

# Визначаємо функцію, яку будемо інтегрувати
def f(t):
    return -np.log(np.cos(t))

# Метод правих прямокутників для обчислення інтегралу
def right_rectangle_method(func, a, b, n):
    h = (b - a) / n
    integral = sum([func(a + i*h) for i in range(1, n+1)]) * h
    return integral

# Визначаємо параметри: кінець інтегралу, кількість підінтервалів та крок
x_end = np.pi / 2  # кінець інтегралу
n = 36  # кількість підінтервалів
h = x_end / n  # крок

# Обчислюємо інтеграл з різними кроками (h та 2h) для подальшої оцінки похибки за правилом Рунге
I_h = right_rectangle_method(f, 0, x_end, n)
I_2h = right_rectangle_method(f, 0, x_end, n//2)

# Обчислюємо похибку за правилом Рунге
R = (I_h - I_2h) / (2**1 - 1)

# Будуємо таблицю та графік
x_vals = np.linspace(0, x_end, n+1)  # значення x для таблиці і графіку
F_vals = [-right_rectangle_method(f, 0, x, n) for x in x_vals]  # значення F(x) для таблиці і графіку

# Виводимо результати
(I_h, I_2h, R, list(zip(x_vals, F_vals)))

# Будуємо графік функції F(x)
plt.figure(figsize=[10,6])
plt.plot(x_vals, F_vals, marker='o', linestyle='-', color='b')
plt.title(r"$F(x) = -\int_{0}^{x} \ln(\cos(t)) \, dt$")
plt.xlabel(r"$x$")
plt.ylabel(r"$F(x)$")
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.xticks(np.arange(0, np.pi/2, np.pi/36))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
