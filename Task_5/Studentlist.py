from Task_5.Students import add_student, show_all, marks, marks_id, delite_student, delite_studentid, edit_student, \
    avarage_s, info_s

ids = 0
student_dict = {}
info_s()
while True:
    prog = input('Enter command: ').lower()
    if prog == 'exit':
        print('Вы вышли из программы')
        break
    elif prog == 'add student':
        ids += 1
        student_dict.update({ids: add_student()})

        add = input('Добавить еще?(y/n) ').lower()
        for i in range(100):
            if add == 'y':
                ids += 1
                student_dict.update({ids: add_student()})
                add = input('Добавить еще?(y/n) ').lower()
            else:
                continue
        print('Students added')
    elif prog == 'show all':
        show_all(student_dict)
    elif prog == 'mark':
        search = input('Поиск по id или фамилии?(id/f): ')
        if search == 'f':
            choice = input('Введите фамилию: ')
            mark = input('Оценка: ')
            marks(student_dict, mark, choice)

            while True:
                add = input('Добавить еще?(y/n) ').lower()
                if add == 'y':
                    choice = input('Введите фамилию: ')
                    mark = input('Оценка: ')
                    marks(student_dict, mark, choice)
                else:
                    break
        else:
            choiceid = int(input('Введите id: '))
            mark = input('Оценка: ')
            marks_id(student_dict, choiceid, mark)
    elif prog == 'edit':
        choice = input('Введите фамилию студента или его id: ')
        edit_student(student_dict, choice)
    elif prog == 'del':
        search = input('Поиск по id или фамилии?(id/f): ')
        if search == 'f':
            choice = input('Введите фамилию студента: ')
            delite_student(student_dict, choice)
        else:
            choiceid = int(input('Введите id: '))
            delite_studentid(student_dict, choiceid)
    elif prog == 'avarage':
        avarage_s(student_dict)
    else:
        print('Такой комманды нет!')