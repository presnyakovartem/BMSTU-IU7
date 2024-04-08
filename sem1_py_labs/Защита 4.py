from math import *

eps = 1e-12

# Приглашние + ввод основных параметров программы
print("Введите начальное значение t: ", end ='')
t_min = float(input())
print("Введите конечное значение t: ", end ='')
t_max = float(input())
print("Введите шаг перебора значений: ", end ='')
h = float(input())

# Форматируем значения под формат 7 знащащих цифр
t_min = float(f"{t_min:.7g}")
t_max = float(f"{t_max:.7g}")
h = float(f"{h:.7g}")

# Проведём проверку праивльности ввода
exst = False
if t_min==t_max or t_min>t_max or h<=0:
    print('Неправильный ввод')

else:
    exst = True
    max_len = 0
    max_lenh = -10000000
    max_f = -1000000000
    min_f = 10000000000

    # Переменная для хранений суммы отриц значений r2
    r2_otr = 0
    for i in range(int(t_min / 1e-55), int((t_max + h - eps) / 1e-55), int(h / 1e-55)):
        # Форматируем значения
        znach = str(float(f'{i * 1e-55:.7g}'))
        znach_f = float(znach)
        r1 = float(f'{0.987 * znach_f ** 3 - 4.01 * znach_f ** 2 + 2.25:.7g}')
        r2 = float(f'{1.02 * znach_f ** 2 - 0.95 * sin(5.2 * znach_f) + 0.57:.7g}')

        # Поиск максимальных и минимальных значений функции и длинны столбца
        max_f = max(max_f, r1)
        min_f = min(min_f, r1)
        max_len = max(len(znach), max_len)

        # Данная строчка неоходима, чтобы узнать максимальную длинну графика
        max_lenh = max(max_lenh, len(znach))
        max_len = max(len(str(r1)), max_len)
        max_len = max(len(str(r2)), max_len)
    # Длинна оси ординат
    len_ord = 60

    # Количество знакомест
    f_interv = (max_f - min_f) / (len_ord - 1)

    #Верхняя строка
    print(' '* len(str(max_lenh)) + str(t_min) + ' '*(len_ord-len(str(t_min)+str(t_max))) + str(t_max))
    print(' '* len(str(min_f)) + '-'*len_ord)

    # Создаём итератор
    iterator = t_min

    # Переменная, хранящая количество иттераций цикла
    for_iterations = int(ceil((((t_max + h + eps) - t_min) // h)))

    # Построние границ графика
    for i in range(int(t_min / 1e-55), int((t_max + h - eps) / 1e-55), int(h / 1e-55)):
        if abs(i * 1e-55) < eps:
            znach = "0"
        else:
            znach = str(float(f"{i * 1e-55:.7g}"))
        ct_z = iterator
        stroka = ""

        # Подсчёт r1
        r1 = cos(ct_z)

        # Добавление столбика со значением i
        stroka += (znach + " " * (max_lenh - len(znach)) + "|")

        left_gr = min_f
        right_gr = left_gr + f_interv

        # Проверка существования тояки
        pt_exist = False

        # Создание строки с точками графика
        for i in range(len_ord):

            # Определение точки
            if ((r1 >= left_gr) and
                    (r1 < right_gr)):
                if pt_exist is False:
                    stroka += "*"
                    pt_exist = True

            # Определение оси абсцисс
            elif ((0 >= left_gr) and
                  (0 < right_gr)):
                stroka += "|"

            # В иных случаях пропускаем данное значение
            else:
                stroka += " "

            left_gr += f_interv
            right_gr += f_interv

        print(stroka)

        iterator += h