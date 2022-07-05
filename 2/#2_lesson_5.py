#A
a = input()
# print(a.count(' '))
count = 0


for i in a:
    if i == ' ':
        count = count + 1
print(count)

z = input()
print(sum(i == ' ' for i in z))

#B
m = input()
t = input()
g = input()
print(f'Привет {m}, АУ! {t} КУку {g}.')
