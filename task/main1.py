from task.fu.Geometry import circle_perimetr, circle_s, triangle_perimetr, triangle_s, cellulose_s, cellulose_perimetr

figure = input('Выберите фигуру: c - circle, t - triangle, cel - cellulose\n')
choice = input('Выберите действие: p, s\n')


if figure == 'c' and choice == 'p':
    r = float(input('Радиус:\n'))
    result = circle_perimetr(r)
    print(f'\nПериметр круга равен \'{result}\'')



elif figure == 'c' and choice == 's':
    r = float(input('Радиус:\n'))
    result = circle_s(r)
    print(f'\nПлощадь круга равна \'{result}\'')

elif figure == 't' and choice == 'p':
    a = float(input('Длина стороны a :\n'))
    b = float(input('Длина стороны b :\n'))
    c = float(input('Длина стороны c :\n'))
    result = triangle_perimetr(a, b, c)
    print(f'\nПериметр треугольника равен \'{result}\'')

elif figure == 't' and choice == 's':
    h = float(input('Высота :\n'))
    result = triangle_s(h)
    print(f'\nПлощадь треугольника равна \'{result}\'')

elif figure == 'cel' and choice == 'p':
    a = float(input('Сторона a:\n'))
    b = float(input('Сторона b:\n'))
    result = cellulose_perimetr(a, b)
    print(f'\nПериметр прямоугольника равен \'{result}\'')

elif figure == 'cel' and choice == 's':
    a = float(input('Сторона a:\n'))
    b = float(input('Сторона b:\n'))
    result = cellulose_s(a, b)
    print(f'\nПлощадь прямоугольника равена \'{result}\'')
else:
    print('Такой фигуры нет!')









