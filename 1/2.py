from calendar import monthrange

def num():
    try:
        year = int(input('Введите год:\n'))
        month = int(input('Введите порядковый номер месяца: \n'))
        num = monthrange(year, month)[1]
        print(num)
    except ValueError:
        print('Нужно ввести целое число!!!')


print('Данная программа покажет вам количество дней')
while True:
    design = str.swapcase(input('Продолжить? \'Y\' or \'N\'\n'))
    if design == 'Y':
        num()

    elif design == 'N':
        print('Goodbye')
        break
    else:
        print('Не понял')






