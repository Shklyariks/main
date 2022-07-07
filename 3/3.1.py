import time

date = input()
try:
    time.strptime(date, '%d.%m.%Y')
    print('OK')
except ValueError:
    print(f'FAILED \n {date} incorrect day')
