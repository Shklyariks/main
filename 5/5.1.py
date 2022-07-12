a = [1, 4, 2, 6, 3, 10, 9, 6]
# a = [input(x) for x in input().split]
for i in range(len(a)):
    # for i in range(1, len(a) -1):
        # if a [i - 1] < a[i] > a[i + 1]

    if int(a[i]) > int(a[i-1]) and int(a[i]) > int(a[i+1]):

        print(int(a[i]))

for i in a:
    if a.count(i) == 1:
        print('Hello')
        print(i)
