a = input().split()
l = []
for i in range(len(a)):
    if i % 3 == 0 and i % 5 != 0:
        l.append(a[i])

print(l)