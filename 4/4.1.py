import math


def func_math(a, b, c):
    d = b ** 2 - 4 * a * c
    print(d)
    if d > 0:
        x1 = int((-b + math.sqrt(d)) / (2 * a))
        x2 = int((-b - math.sqrt(d)) / (2 * a))
        print(x1, x2)

    elif d == 0:
        x = int(-b / (2 * a))
        print(x)
    else:
        print("Корней нет")
    return


m = input().split()
l = []
for i in range(len(m)):
    a = int(m[0])
    b = int(m[1])
    c = int(m[2])
func_math(a, b, c)


