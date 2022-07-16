import json
with open('victorina.json', mode='r', encoding='utf8') as json_file:
    data = json.load(json_file)
    #v1 = data.get('v1')
    #print(v1)
    date, v1, v2, v3 = [i for i in data.values()]
    print(v1)
    if v1 == 'Золушка':
        print("Верно")
    if v2 == 'Один дома':
        print('Верно')
    if v3 == 'Спанч Боб':
        print('Верно')
    else:
        print('Не верно')
