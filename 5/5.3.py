a = input()
my_dict = {}
for i in a.split(' '):
    my_dict.update({i: a.count(i)})
print(my_dict)
