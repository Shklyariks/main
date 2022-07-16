import math

import matplotlib.pyplot as plt


def func_math(a, b, c):
    global x
    d = b ** 2 - 4 * a * c
    xk = []
    yk = []
    # plt.plot(xk, yk)
    # plt.show()

    print(d)
    if d > 0:
        x = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)

    elif d == 0:
        x = -b / (2 * a)
        print(x)

    else:
        print("Корней нет")
    return x


def f(x, a, b, c):
    return (a * x ** 2) + (b * x) + c


m = input().split()

for i in range(len(m)):
    a = float(m[0])
    b = float(m[1])
    c = float(m[2])

x = func_math(a, b, c)

f(x, a, b, c)

x_coords = [x for x in range(-10, 10, 1)]

y_coords = []
for x in x_coords:
    y_coords.append(f(x, a, b, c))

plt.plot(x_coords, y_coords)
plt.show()