import time

date = input()


def time_func(date):
    try:
        time.strptime(date, '%d.%m.%Y')
        print('OK')
    except ValueError:
        print(f'FAILED \n {date} incorrect day')
    return date


time_func(date)
