num = int(input())

def df(a):
    result = []
    for i in range(1, int(a / 2) + 1): # Цикл от 1 до num
        if a % i == 0:
            result.append(i)
    return result

def perf(result):
    if sum(result) == num:
        print('Число совершенное')








