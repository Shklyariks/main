#A
def counter():
    a = int(input('Введите число \'a\': \n'))
    b = int(input('Введите число \'b\': \n'))
    d = input('Действие: \'+\', \'-\', \'*\', \'/\' \n')
    if d == '+':
        r = a + b
        print(r)
    elif d == '-':
        r = a - b
        print(r)
    elif d == '*':
        r = a * b
        print(r)
    elif d == '/':
        r = a / b
        print(r)

counter()

#B
def vklad(n,m):
    s = (n * 0.1 * m)/100
    r = (s + n)
    print(s)
    print(r)

n = float(input('Размер вклада: \n'))
m = float(input('Количество лет: \n'))
vklad(n,m)