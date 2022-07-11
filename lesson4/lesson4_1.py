from calendar import monthrange
import datetime



def num_1(year, month):
    try:
        date = datetime.date(1900, month, 1).strftime('%B')
        num = monthrange(year, month)[1]
        return num
    except ValueError:
        print('Нужно ввести целое число!!!')
