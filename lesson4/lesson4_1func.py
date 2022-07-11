from lesson4.lesson4_1 import num_1


def entering():

    print('Данная программа покажет вам количество дней')
    while True:
        design = str.swapcase(input('Продолжить? \'Y\' or \'N\'\n'))
        if design == 'Y':
            year = int(input('Введите год:\n'))
            month = int(input('Введите порядковый номер месяца: \n'))
            num_1(year, month)

        elif design == 'N':
            print('Goodbye')
            break
        else:
            print('Не понял')