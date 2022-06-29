from calendar import monthrange
import datetime

def num():
    try:
        year = int(input('Введите год:\n'))
        month = int(input('Введите порядковый номер месяца: \n'))
        date = datetime.date(1900, month, 1).strftime('%B')
        num = monthrange(year, month)[1]
        print(date)
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






