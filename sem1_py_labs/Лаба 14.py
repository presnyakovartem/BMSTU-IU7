# Пресняков А.К. ИУ7-13Б. Лабораторная работа 14
# Написать программу, которая позволит с помощью меню выполнить
# действия с бинарными файлами:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных
# 3. Вывести содержимое базы данных
# 4. Добавить запись в произвольное место базы данных
# 5. Удалить произвольную запись из базы данных
# 6. Поиск по одному полю
# 7. Поиск по двум полям

import struct
from string import *

# МЕНЮ
def menu(file):
    print()
    if file is None:
        print("Файл не выбран")

    else:
        print(file)

    print()
    print("Список команд:")
    print("1. Выбрать файл для работы")
    print("2. Инициализировать базу данных")
    print("3. Вывести содержимое базы данных")
    print("4. Добавить запись в выбранную позицию базы данных")
    print("5. Удалить запись с выбранной позиции базы данных")
    print("6. Поиск по одному полю")
    print("7. Поиск по двум полям")
    print()
    print("0. Выход")
    print()
    user_charge = charge_input()
    print()
    return user_charge

# Разветвлитель дейсвтий
def charge_performer(charge, file):
    if charge == 1:
        res = file_choose(file)

        if res is not False:
            return ["file", res]

        else:
            return ['bool', False]

    elif charge == 2:
        res = db_initialize()
        return ['file',res]

    elif charge == 3:
        res = output_db(file)

        if res is not False:
            return ["bool", res]

        else:
            return ['bool', False]

    elif charge == 4:
        res = add_stroke(file)
        return ["bool", res]

    elif charge == 5:
        res = delete_writing(file)
        return ["bool", res]

    elif charge == 6:
        res = field_search(file)
        return ["bool", res]

    elif charge == 7:
        res = two_field_search(file)
        return ["bool", res]


# 1. Выбор файла
def file_choose(file):
    filename = filename_input()
    print()
    try:
        a = open(filename)
        a.close()

    except Exception:
        print("Файл не сущетсвует, либо у вас нет доступа к файлу")
        return False

    else:

        if database_check(filename):
            return filename

        else:
            print("Некорректный формат базы данных")
            return False

# 2. Инициализация БД
def db_initialize():
    name = filename_input()

    with open(name, '+wb') as f:
        stroke_count = input_int_strokework("Введите кол-во строк: ")

        for i in range(stroke_count):
            stroke_database = stroke_create()

            stroke_database = convert_format().pack(*stroke_database)
            f.write(stroke_database)

    return name

# 3. Вывести содержимое БД
def output_db(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False

    else:
        with open(filename, 'rb') as f:

            # Вывод названий столбцов
            print('-' * 85)
            titles = ['ID', 'Name', 'Rating', 'Rank']
            id_t = f'{titles[0]:^20}|'
            name = f'{titles[1]:^20}|'
            rating = f'{titles[2]:^20}|'
            rank = f'{titles[3]:^20}|'
            out = '|' + id_t + name + rating + rank
            print(out)

            while (stroke_data := f.read(convert_format().size)) != b'':
                stroke_data = convert_format().unpack(stroke_data)

                # Вывод строки
                print('-' * 85)
                out = '|'
                for i in range(4):
                    if str(stroke_data[i]).isdigit():
                        out += f'{str(stroke_data[i]):^20}|'

                    else:
                        s = stroke_data[i].decode().replace('\x00', '')
                        out += f'{s:^20}|'
                print(out)
            print('-' * 85)

        return True

#4. Добавление записи в БД
def add_stroke(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False

    stroke_add = stroke_create()
    stroke_add = convert_format().pack(*stroke_add)
    with open(filename, 'rb') as f:
        stroke_count = 0
        while (a := f.read(convert_format().size)) != b'':
            stroke_count += 1
    print(stroke_count)
    while (position := input_int_strokework('Введите положение новой строки: ')) > stroke_count + 1:
        print("Такой позиции нет")

    with open(filename, '+rb') as f:
        f.seek(convert_format().size * (position - 1))
        f.write(stroke_add)

    return True

# 5. Удаление строки БД
def delete_writing(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False
    with open(filename, 'rb') as f:
        stroke_count = 0
        while (a := f.read(convert_format().size)) != b'':
            stroke_count += 1

        if stroke_count == 0:
            print("Файл пуст!")
            return True

    while (position := input_int_strokework('Введите номер удаляемой строки: ')) > stroke_count:
        print("Такой строки не существует")

    with open(filename, '+rb') as f:
        f.seek(convert_format().size * position)

        while (move_stroke := f.read(convert_format().size)) != b'':
            f.seek(f.tell() - convert_format().size * 2)
            f.write(move_stroke)
            f.seek(f.tell() + convert_format().size)

        f.truncate(convert_format().size * (stroke_count - 1))

    return True

# 6. Поиск по одному полю
def field_search(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False

    with open(filename, 'rb') as f:
        print('1. ID')
        print('2. Name')
        print('3. Rating')
        print('4. Rank')
        num = charge_input()

        if num in [1, 3]:
            search_word = input_int_element('Введите число: ')

        elif num in [2, 4]:
            search_word = input_string_element('Введите строку: ')

        else:
            print("Столбца с таким номером нет!")
            return False

        index_column = num - 1

        print('-' * 85)
        titles = ['ID', 'Name', 'Rating', 'Rank']
        id_t = f'{titles[0]:^20}|'
        name = f'{titles[1]:^20}|'
        rating = f'{titles[2]:^20}|'
        rank = f'{titles[3]:^20}|'
        out = '|' + id_t + name + rating + rank
        print(out)
        while (stroke_data := f.read(convert_format().size)) != b'':
            stroke_data = convert_format().unpack(stroke_data)

            if num in [1, 3]:
                if stroke_data[index_column] == search_word:
                    print('-' * 85)
                    out = '|'
                    for i in range(4):
                        if str(stroke_data[i]).isdigit():
                            out += f'{str(stroke_data[i]):^20}|'

                        else:
                            s = stroke_data[i].decode().replace('\x00', '')
                            out += f'{s:^20}|'
                    print(out)

            else:
                if stroke_data[index_column].decode().replace('\x00', '') == search_word:
                    print('-' * 85)
                    out = '|'
                    for i in range(4):
                        if str(stroke_data[i]).isdigit():
                            out += f'{str(stroke_data[i]):^20}|'

                        else:
                            s = stroke_data[i].decode().replace('\x00', '')
                            out += f'{s:^20}|'
                    print(out)
        print('-' * 85)

    return True

# 7. Поиск по двум полям
def two_field_search(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False

    with open(filename, 'rb') as f:
        print("Введите первый столбец поиска: ")
        print('1. ID')
        print('2. Name')
        print('3. Rating')
        print('4. Rank')
        num1 = charge_input()

        if num1 in [1, 3]:
            search_word1 = input_int_element('Введите число: ')

        elif num1 in [2, 4]:
            search_word1 = input_string_element('Введите строку: ')

        else:
            print("Столбца с таким номером нет!")
            return False

        index_column1 = num1 - 1
        print("Введите втотрой столбец поиска: ")
        print('1. ID')
        print('2. Name')
        print('3. Rating')
        print('4. Rank')
        num2 = charge_input()

        if num2 in [1, 3]:
            search_word2 = input_int_element('Введите число: ')

        elif num2 in [2, 4]:
            search_word2 = input_string_element('Введите строку: ')

        else:
            print("Столбца с таким номером нет!")
            return False

        index_column2 = num2 - 1

        if index_column1 == index_column2:
            print("Вы ввели одинаковые столбцы, поиск невозможен!")
            return False

        print('-' * 85)
        titles = ['ID', 'Name', 'Rating', 'Rank']
        id_t = f'{titles[0]:^20}|'
        name = f'{titles[1]:^20}|'
        rating = f'{titles[2]:^20}|'
        rank = f'{titles[3]:^20}|'
        out = '|' + id_t + name + rating + rank
        print(out)
        while (stroke_data := f.read(convert_format().size)) != b'':
            stroke_data = convert_format().unpack(stroke_data)
            flag = True
            if (index_column1 + 1) in [1, 3]:
                if stroke_data[index_column1] == search_word1:
                    pass

                else:
                    flag = False
            else:
                if stroke_data[index_column1].decode().replace('\x00', '') == search_word1:
                    pass

                else:
                    flag = False

            if (index_column2 + 1) in [1, 3]:
                if stroke_data[index_column2] == search_word2:
                    pass

                else:
                    flag = False
            else:
                if stroke_data[index_column2].decode().replace('\x00', '') == search_word2:
                    pass

                else:
                    flag = False

            if flag is True:
                print('-' * 85)
                out = '|'
                for i in range(4):
                    if str(stroke_data[i]).isdigit():
                        out += f'{str(stroke_data[i]):^20}|'

                    else:
                        s = stroke_data[i].decode().replace('\x00', '')
                        out += f'{s:^20}|'
                print(out)
        print('-' * 85)
    return True

# Ввод натурального числа
def natural_int_input(stroke):
    natural = None
    while natural is None:

        try:
            natural = int(input(stroke))

        except Exception:
            print("Число введено некорректно. Попробуйте ещё раз!")
            natural = None

        else:

            if natural <= 0:
                print("ЧИсло не может быть меньше или равно нулю. Попробуйте ещё раз!")
                natural = None

            else:
                return natural

# Ввод целочисленного элемента БД
def input_int_element(stroke):
    integer = None
    while integer is None:
        integer = input(stroke)

        if integer.isdigit():
            if int(integer) > 1e20:
                print('Число не может быть такой большой длинны')
                integer = None

            else:
                pass

        else:
            print('Введённое число не является числом или содержит на концах пробелы')
            integer = None

    return int(integer)

# Ввод строчного элемента БД
def input_string_element(stroke):
    a = None
    while a is None:
        a = input(stroke)

        if a.isdigit():
            print('Строка не может быть числом')
            a = None
        elif a == '':
            print('Строка не может быть пустой')
            a = None
        elif len(a) == a.count(' '):
            print('Строка не может состоять из пробелов')
            a = None
        elif len(a) >= 2 and (a[0] == ' ' or a[-1] == ' '):
            print('Строка не может иметь на концах пробелы')
            a = None
        elif len(a) > 20:
            print("Строка не может длиннее 20 символов")
            a = None

    return a

# Проверка на корректность числа
def input_int_strokework(stroke):
    a = None
    while a is None:
        try:
            a = int(input(stroke))

        except Exception:
            print('Число введено некорректно')

        else:
            if a < 1:
                print("Число не может быть меньше одного")
                a = None

    return int(a)

# Ввод команды пользователем
def charge_input():
    charge = None
    while charge is None:

        try:
            charge = int(input("Введите номер команды: "))

        except ValueError:
            print("Вы ввели не число! Повторите ввод.")
            charge = None

        else:

            if charge < 0 or charge > 7:
                print("Команды под таким номером не существует! Повторите ввод.")
                charge = None

    return charge

# Ввод команды пользователем
def database_charge_input():
    charge = None
    while charge is None:

        try:
            print("Выберите формат выбора файла")
            print("1. Директория")
            print("2. Название")
            charge = int(input("Введите номер команды: "))

        except ValueError:
            print("Вы ввели не число! Повторите ввод.")
            charge = None

        else:

            if charge < 1 or charge > 2:
                print("Команды под таким номером не существует! Повторите ввод.")
                charge = None

    return charge

# Ввод названия файла
incorrect_link_alphabet = '$/:*?<>|+.'
incorrect_filename_alphabet ='$\/:*?<>|+.'
def filename_input():
    filename = None
    id = database_charge_input()
    print()
    if id == 2:

        while filename is None:

            try:
                filename = input("Введите название файла: ")

            except Exception:
                print("В названии файла присутствуют некорректные символы для имени файла. Попробуйте ещё раз!")
                print(f"Некорректные символы: {incorrect_filename_alphabet}")

            else:

                for k in incorrect_filename_alphabet:

                    if k in filename:
                        print("В названии файла присутствуют некорректные символы для имени файла. Попробуйте ещё раз!")
                        filename = None
                        break

        filename+=".bin"
        return filename
    if id == 1:

        while filename is None:

            try:
                filename = input("Введите название файла: ")

            except Exception:
                print("Ссылка указана некорректно. Попробуйте ещё раз")
                print(f"Некорректные символы: {incorrect_link_alphabet }")

            else:

                for k in incorrect_link_alphabet:

                    if k in filename:
                        print("В ссылке присутствуют некорректные символы для имени файла. Попробуйте ещё раз!")
                        filename = None
                        break
                    if ".bin" not in filename:
                        print("Расширение .bin должно присутствовать при создании ссылки!")
                        filename = None
                        break
        return filename

# Проверка корректности базы данных
def database_check(fname):
    with open(fname, 'rb') as f:
        try:
            while (stroke_data := f.read(convert_format().size)) != b'':
                stroke_data = convert_format().unpack(stroke_data)

                if not (str(stroke_data[0]).isdigit() and str(stroke_data[2]).isdigit()):
                    return False

                if str(stroke_data[1]).isdigit() or str(stroke_data[3]).isdigit():
                    return False

        except Exception:
            return False

        else:
            return True

# Создание строки
def stroke_create():
    stroke_elements = []

    # Запись первого элемента
    element = input_int_element("Введите ID персонажа: ")
    stroke_elements.append(element)

    # Запись второго элемента
    element = input_string_element("Введите имя персонажа: ")
    stroke_elements.append(element.encode())

    # Запись третьего элемента
    element = input_int_element("Введите рейтинг персонажа: ")
    stroke_elements.append(element)

    # Запись четвёртого элемента
    element = input_string_element("Введите звание персонажа: ")
    stroke_elements.append(element.encode())

    return stroke_elements

# Перевод в шаблон строки бинарной БД
def convert_format():
    return struct.Struct('i 20s i 20s')

# Старт программы
file = None
while True:
    charge = menu(file)
    if charge == 0:
        break

    else:
        result = charge_performer(charge, file)

        if result[0] == 'file':
            file = result[1]
print("Спасибо за выбор программы!")