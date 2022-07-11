a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print('Условие 1')
    print(a, b, c)
elif b < c < a:
    print('Условие 2')
    print(b, c, a)
elif b < a < c:
    print('Условие 3')
    print(b, c, a)
elif a < c < b:
    print('Условие lesson4')
    print(a, c, b)
elif c < b < a:
    print('Условие 5')
    print(c, b, a)

