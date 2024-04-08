# Пресняков Артём ИУ7-13Б
# Защита 5-й лабы

from math import *

# Ввод шага вывода
step = int(input("Введите шаг вывода: "))

# Ввод точности
equancy = float(input("Введите точность: "))

# Ввод количества
iterations = int(input("Введите количество итераций: "))

# Проверка корректности введённых данных
exst = False
if step < 1:
    print("Ошибка: неверный ввод шага")

elif equancy <= 0:
    print('Ошибка: неверный ввод погрешности')

elif iterations < 1:
    print('Ошибка: неверный ввод количества итераций')

else:
    exst = True

# Создадим список, в котором будут храниться значения членов ряда
if exst is True:
    t = []
    t_str = []
    t_max = None
    iterator = 1

    # Произведём подсчёт значений членов ряда и запишем их в список
    for i in range(1, iterations+1):
        t_current = (1 / iterator)
        iterator += i
        t.append(t_current)

        # Поиск максимального члена последовательности для построения таблицы
        t_str.append(str(f'{t_current:.7g}'))
        t_max = max(t_str, key=len)


    # Узнаем длину конечной суммы(для построения таблицы)
    s_max = str(sum(t))

    # Начнём построение таблицы
    upper = '-' * (4 + 11 + len(t_max) + 8 + len(s_max) + 8)
    title = ('|' + '№ Итерации ' + '|' + ' ' * floor((len(t_max) + 8)/2) +
             'x' + ' '*(len(t_max) + 8 - (len(t_max)+8)//2-1) + '|' +
             ' '*floor((len(s_max) + 8)/2) + 'S' +
             ' '*(len(s_max) + 8 - (len(s_max)+8)//2-1) + '|')
    print(upper)
    print(title)
    print(upper)

    # Вводим счётчик количества итераций
    ct_iter = 0
    is_Reached = False
    # Начнём вывод значений в таблицу при помощи цикла for
    for i in range(0, len(t), step):

        # Форматируем значения для вывода
        t_current = str(f'{t[i]:.7g}')
        s_current = str(f'{sum(t[:i+1]):.7g}')
        stroke = ('| ' +  str(int(i+1)) + ' ' * (10-len(str(i+1))) +
                  '|' + ' ' * ((len(t_max) + 8) // 2 - len(t_current) // 2) + t_current +
                  ' ' * (len(t_max) + 8 - (len(t_max) + 8) // 2 - (len(t_current) - len(t_current) // 2)) +
                  '|' + ' ' * ((len(s_max) + 8) // 2 - len(s_current) // 2) + s_current +
                  ' ' * (len(s_max) + 8 - (len(s_max) + 8) // 2
                         - (len(s_current) - len(s_current) // 2)) + '|')

        # Проверка на достижение точности
        if abs(sum(t[:i+1])) <= equancy:
            is_Reached = True
            break
        print(stroke)
        ct_iter+=1

    print(upper)

    # Вывод
    if is_Reached is True:
        print('Погрешность достигнута за ' + str(ct_iter) + ' итераций')

    else:
        print('Погрешность не достигнута')