a = input().split()
l = []
'''for i in range(len(a)):
    if int(a[i]) % 3 == 0 and int(a[i]) % 5 != 0:
        l.append(a[i])

print(l)'''

for i in a:
    if int(i) % 3 == 0 and int(i) % 5 != 0:
        l.append(i)
print(l)


z = input().split()
li = []
for i in z:
    if z.count(i) <= 1:
        li.append(i)
print(li)

