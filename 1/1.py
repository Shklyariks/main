print('Введите число или введите \'x\' чтобы завершить')
while True:
    try:
        a = input('Введите число: ')
        if a == 'x':
            print('Программа завершена')
            break
        elif float(a) > 0:
            print('Положительное')
        elif float(a) == 0:
            print('0')
        else:
            print('Отрицательное')
    except ValueError:
        print('Это не число')
        print('Введите число или введите \'x\' для завершения программы')

