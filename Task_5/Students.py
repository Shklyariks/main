from statistics import mean


def add_student():
    while True:
        try:
            first_name = input('Введите фамилию:\n ').capitalize()
            name = input('Введите имя:\n').capitalize()
            patronymic = input('Введите очество:\n').capitalize()
            age = int(input('Возраст:\n'))
            students_list = [[first_name, name, patronymic, age]]
            return students_list
        except ValueError:
            print('Нужно ввести количество лет')


def show_all(student_dict):
    if student_dict == {}:
        print('Список пуст')
    else:
        for k, v in student_dict.items():
            for i in v:
                print(f'id: {k}, first_name: {i[0]}, name: {i[1]}, patronymic: {i[2]}, age: {i[3]}')


def marks(student_dict, mark, choice):
    for k in student_dict.values():
        if choice in k[0]:
            for i in k:
                if len(i) > 4:
                    for m in i[4].values():
                        m.append(int(mark))
                else:
                    marks = {'marks': [int(mark)]}
                    k[0].append(marks)
    print(student_dict)


def marks_id(student_dict, choiceid, mark):
    if choiceid in student_dict:
        for k in student_dict[choiceid]:
            if len(k) > 4:
                for m in k[4].values():
                    m.append(int(mark))
            else:
                marks = {'marks': [int(mark)]}
                k.append(marks)
    else:
        print('Студент не найден')
    print(student_dict)

def delite_student(student_dict, choice):

    for k, v in list(student_dict.items()):
        for i in v:
            if choice in i[0]:
                del student_dict[k]
                print('Студент удален')
            else:
                print('Студент не найден')

def delite_studentid(student_dict, choiceid):

    if choiceid in student_dict:
        del student_dict[choiceid]
    else:
        print('Студент не найден')


def edit_student(student_dict, choice):
    for k, v in student_dict.items():
        for i in v:
            if choice in i[0] or choice in student_dict:
                a = input("Редактировать фамилию(f), имя(n), Отчество(o), Возраст(y), Редактировать все(all): ")
                if a == 'f':
                    i[0] = input('Введите фамилию: ')
                elif a == 'n':
                    i[1] = input('Введите имя: ')
                elif a == 'o':
                    i[2] = input('Введите отчество: ')
                elif a == 'y':
                    i[3] = int(input('Введите возраст: '))
                else:
                    z = input('Введите фио и возраст студента: ').split()
                    i[0] = z[0]
                    i[1] = z[1]
                    i[2] = z[2]
                    i[3] = z[3]
            print(f'id: {k}, first_name: {i[0]}, name: {i[1]}, patronymic: {i[2]}, age: {i[3]}')


def avarage_s(student_dict):

    avarage = []
    for k, v in student_dict.items():
        for i in v:
            if len(i) > 4:
                for z in i[4]['marks']:
                    avarage.append(z)

    list_avg = mean(avarage)

    print(f'Средний бал студентов: {list_avg} ')

def info_s():
    print('exit - Выйти из программы')
    print('add student - Добавить студента')
    print('show all - Показать список студентов')
    print('mark - Поставить оценку')
    print('del - Удалить студента из журнала')
    print('edit - Редактировать информацию постуденту')
    print('avarage - Средний балл')
    return
