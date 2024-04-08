# Пресняков А.К. ИУ7-13Б. Лабораторная работа 13
# Требуется написать программу, которая позволит с помощью меню выполнить
# следующие действия:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
# его записями)
# 3. Вывести содержимое базы данных
# 4. Добавить запись в конец базы данных
# 5. Поиск по одному полю
# 6. Поиск по двум полям

from string import *

incorrect_link_alphabet = '$/:*?<>|+.'
incorrect_filename_alphabet ='$\/:*?<>|+.'

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
    print("4. Добавить запись в конец базы данных")
    print("5. Поиск по одному полю")
    print("6. Поиск по двум полям")
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
        res = field_search(file)
        return ["bool", res]

    elif charge == 6:
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

    stroke_count = natural_int_input("Введите количество строк: ")

    column_count = natural_int_input("Введите количество столбцов: ")

    create_database(stroke_count, column_count, name)
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
        f = open(filename, 'r')
        stroka = f.readline()
        stroka = stroka.split(";")
        stroka[1] = stroka[1][:len(stroka[1]) - 1]
        stroke = int(stroka[0])
        column = int(stroka[1])
        print("-" * (20 * column + column + 1))
        for i in range(stroke + 1):
            output = '|'
            stroka = f.readline()
            stroka = stroka.split("*")
            stroka[-1] = stroka[-1][:len(stroka[-1]) - 1]

            for i in range(column):
                output += f'{stroka[i]:^20}|'
            print(output)
            print("-" * (20 * column + column + 1))
        f.close()
        return True

#4. Добавление записи в конец БД
def add_stroke(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False

    c = find_column_count(filename)
    titles = find_titles(filename)
    stroke = add_stroke_create(c,titles)
    f = open(filename, "a")
    f.write(stroke + '\n')
    f.close()
    lenth_change(filename)
    return True

# 5. Поиск по одному полю
def field_search(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False
    column1 =  column_input(filename, "Введите название столбца: ")
    word = database_element_input("Введите строку, которая будет искаться: ")
    word = word.lower()
    f = open(filename, 'r')
    stroke = f.readline()
    stroke = stroke.split(";")
    s = int(stroke[0])
    column = int(stroke[1])
    print("-" * (20 * column + column + 1))
    output = '|'
    stroke = f.readline()
    stroke = stroke.split("*")
    stroke[-1] = stroke[-1][:len(stroke[-1]) -1]
    for i in range(column):
        output += f"{stroke[i]:^20}|"
    print(output)
    for i in range(s):
        stroke = f.readline()
        stroke = stroke.split("*")
        stroke[-1] = stroke[-1][:len(stroke[-1]) - 1]
        check = [j.lower() for j in stroke]
        if word == check[column1]:
            print("-" * (20 * column + column + 1))
            output = '|'
            for i in range(column):
                output += f"{stroke[i]:^20}|"
            print(output)

    print("-" * (20 * column + column + 1))
    f.close()
    return True

# 6. Поиск по двум полям
def two_field_search(filename):
    if filename is None:
        print("Файла не существует")
        return False

    elif database_check(filename) is False:
        print("Файл не содержит базу данных в необходимом формате")
        return False

    column1 =  column_input(filename, "Введите название столбца 1: ")
    word1 = database_element_input("Введите строку, которая будет искаться: ")
    word1 = word1.lower()

    column2 = None
    while column2 is None:
        column2 = column_input(filename, "Введите название столбца: ")

        if column1 == column2:
            print("Столбцы не могут совпадать, попробуйте ещё раз")
            column2 = None

    word2 = database_element_input("Введите строку, которая будет искаться: ")
    word2 = word2.lower()
    if filename is None:
        print("Файла не существует")
        return False

    f = open(filename, 'r')
    stroke = f.readline()
    stroke = stroke.split(";")
    s = int(stroke[0])
    column = int(stroke[1])

    print("-" * (20 * column + column + 1))
    output = '|'
    stroke = f.readline()
    stroke = stroke.split("*")
    stroke[-1] = stroke[-1][:len(stroke[-1]) - 1]
    for i in range(column):
        output += f"{stroke[i]:^20}|"
    print(output)
    for i in range(s):
        stroke = f.readline()
        stroke = stroke.split("*")
        stroke[-1] = stroke[-1][:len(stroke[-1]) - 1]
        check = [j.lower() for j in stroke]
        if word1 == check[column1] and word2 == check[column2]:
            print("-" * (20 * column + column + 1))
            output = '|'
            for i in range(column):
                output += f"{stroke[i]:^20}|"
            print(output)

    print("-" * (20 * column + column + 1))
    f.close()
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

            if charge < 0 or charge > 6:
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

        filename+=".txt"
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
        return filename

# Ввод элемента базы данных
def database_element_input(stroke):
    a = None
    while a is None:

        try:
            a = input(stroke)

        except Exception:
            print("Некорректный ввод. Попробуйте ещё раз")

        else:

            for k in incorrect_filename_alphabet:

                if k in a:
                    print("Некорректные символы при вводе. Попробуйте ещё раз!")
                    a = None
                    break

            if a is not None and len(a) > 20:
                print("Максимальная длинна ввода - 20 символов, попробуйте ещё раз!")
                a = None

            elif a is not None and len(a) > 0 and (a[0] == ' ' or a[-1] == ' '):
                print("На концах ввода не может быть пробелов, попробуйте ещё раз!")
                a = None

            elif a is not None and a == '':
                print("Вы ничего не ввели, попробуйте ещё раз")
                a = None
    return a

# Проверка корректности базы данных
def database_check(fname):
    f  = open(fname, 'r')
    line = f.readline()
    try:
        line = line.split(";")

        if len(line) != 2:
            return False

        line[1] = line[1][:len(line[1]) - 1]
        stroke = int(line[0])
        column = int(line[1])

    except Exception:
        return False

    try:

        for m in range(stroke + 1):
            line = f.readline()
            line = line.split("*")

            if len(line) != column:
                return False

    except Exception:
        return False

    return True

# Ввод колонки таблицы
def column_input(fname, title):
    f = open(fname, 'r')
    stroke = f.readline()
    stroke = f.readline()
    stroke = stroke.split("*")
    stroke[-1] = stroke[-1][:len(stroke[-1]) - 1]
    stroke = [s.lower() for s in stroke]
    column = None
    while column is None:
        column = database_element_input(title)
        column = column.lower()

        if column in stroke:
            column = stroke.index(column)

        else:
            print("Такого стоблца нет")
            column = None

    f.close()

    return column

# Создание заголовков стоблцов
def title_create(n):
    stroke = ''
    for i in range(n):
        element = database_element_input(f"Введите название {i+1}-го столбца: ")
        stroke += f'{element}*'

    stroke = stroke[:len(stroke) - 1]
    return stroke

# Создание строки
def stroke_create(c,s, types):
    stroke = ''
    for i in range(c):
        if types[i] == "str":
            element = database_element_input(f"Введите строку {i+1}-го столбца {s+1}-й строки: ")
            stroke+=f"{element}*"
        else:
            while True:
                element = database_element_input(f"Введите число {i + 1}-го столбца {s + 1}-й строки: ")
                try:
                    element1 = int(element)
                except ValueError:
                    print("Вы ввели не число, попробуйте ещ раз")
                else:
                    break
            stroke += f"{element}*"

    stroke = stroke[:len(stroke) - 1]
    return stroke

# Создание дополнительной строки
def add_stroke_create(c, types):
    stroke = ''
    for i in range(c):
        if i==1:
            element = database_element_input(f"Введите элемент {i + 1}-го нового стоблца: ")
            stroke += f"{element}*"
        else:
            while True:
                element = database_element_input(f"Введите число {i + 1}-го столбца строки: ")
                try:
                    element1 = int(element)
                except ValueError:
                    print("Вы ввели не число, попробуйте ещ раз")
                else:
                    break
            stroke += f"{element}*"

    stroke = stroke[:len(stroke) - 1]
    return stroke

# Создание базы данных
def create_database(s,c, fname):
    f = open(fname, 'w+')
    f.write(f'{s};{c}\n')
    stroke = title_create(c)
    types = column_types(stroke,)
    f.write(stroke + "\n")
    for num in range(s):
        f.write(stroke_create(c,num,types) + '\n')

    f.close()

def column_types(stroke):
    stroke = stroke.split("*")
    types = []
    for i in range(len(stroke)):
        type = input(f"Введите тип данных для столбца {stroke[i]} (str или int): ")
        types.append(type)
    return types

def find_column_count(fname):
    f = open(fname, 'r')
    stroke = f.readline()
    f.close()
    stroke = stroke.split(";")
    stroke[1] = stroke[1][:len(stroke[1]) - 1]
    return int(stroke[1])

def find_titles(filename):
    f = open(filename, 'r')
    stroke = f.readline()
    stroke = f.readline()
    stroke = stroke.split("*")
    return stroke

# Изменение длины
def lenth_change(fname):
    f = open(fname, 'r')
    stroke_list = []

    stroke = f.readline()
    stroke = stroke.split(";")

    stroke[0] = str(int(stroke[0]) + 1)
    s = int(stroke[0])

    stroke = stroke[0] + ';' + stroke[1]
    stroke_list.append(stroke)
    for i in range(s+1):
        stroke = f.readline()
        stroke_list.append(stroke)

    f.close()

    f = open(fname, "w+")
    f.writelines(stroke_list)
    f.close()
    return True



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