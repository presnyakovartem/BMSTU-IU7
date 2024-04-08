# Пресняков Артём ИУ7-13Б. Лабороторная 4.21 вариант.
# Построить таблицу значений 2-х функций
# Построить график одной из функций
# *Вычислить сумму отрицательных значений функции r2

from math import *

eps = 1e-12

pr = 1

# Приглашние + ввод основных параметров программы
print("Введите начальное значение t: ", end ='')
t_min = float(input())
print("Введите конечное значение t: ", end ='')
t_max = float(input())
print("Введите шаг перебора значений: ", end ='')
h = float(input())

# Проведём проверку праивльности ввода
exst = False
if t_min == t_max:
    print('Неправильный ввод: начальное и конечное значение не могут быть равны')

elif t_min > t_max:
    print('Неправильный ввод: начальное значение не может быть больше конечного')

elif h < 0:
    print('Неправильный ввод: шаг не может быть меньше нуля')
else:
    exst = True

# Начнём построение таблицы
if exst== True:

    # Необходимо вычислить максимальную длину столбца таблицы, а также значения
    # функции для дальнейшего построения графика функции
    max_len = 0
    max_lenh = float('-inf')
    max_f = float('-inf')
    min_f = float('+inf')

    # Переменная для хранений суммы отриц значений r2
    r2_sum = 0

    # Создаём итератор
    iterator = t_min

    # Переменная, хранящая количество иттераций цикла
    iterations = int(ceil((((t_max + h + eps) - t_min) // h)))

    for i in range(iterations):

        # Форматируем значения
        znach = str(float(f'{iterator:.7g}'))
        znach_f = iterator*pr

        # Вычисление погрешности (ПРИ НАЛИЧИИ)
        if (h - int(h)) < 1e-7 and (h - int(h)) != 0:
            pr = (1e-7 / (h - int(h)) * 100)

        r1 = 0.987 * znach_f ** 3 - 4.01 * znach_f ** 2 + 2.25
        r2 = 1.02 * znach_f ** 2 - 0.95 * sin(5.2 * znach_f) + 0.57

        #Поиск максимальных и минимальных значений функции и длинны столбца
        max_f = max(max_f,r1)
        min_f = min(min_f,r1)
        max_len = max(len(znach),max_len)

        # Данная строчка неоходима, чтобы узнать максимальную длинну графика
        max_lenh = max(max_lenh, len(znach))
        max_len = max(len(str(r1)),max_len)
        max_len = max(len(str(r2)),max_len)
        iterator+=h

    # Строим шапочку таблицы
    upper = '-' * (4 + 3*(max_len + 8))
    title = ('|' + ' '*floor((max_len+8)/2) + 'h' +
                 ' '*(max_len + 8 - (max_len+8)//2-1)
                 + '|' + ' '*floor((max_len+8)/2) + 'r1' +
                 ' '*(max_len + 8 - 1 - (max_len+8)//2-1) +
                 '|' + ' ' * floor((max_len + 8) / 2) + 'r2' +
                 ' ' * (max_len + 8 - 1 - (max_len + 8) // 2 - 1) + '|')
    print(upper)
    print(title)
    print(upper)

    # Создаём итератор
    iterator = t_min

    # Переменная, хранящая количество иттераций цикла
    iterations = int(ceil((((t_max + h + eps) - t_min) // h)))

    # Строим основную таблицу
    for j in range(iterations):

        # Подсчёт значений + форматирование значений для таблицы
        hzn = iterator*pr
        if abs(hzn)<eps:
            h0 = '0'
        else:
            h0 = str(f'{iterator:.7g}')
        r1 = str(float(f'{0.987 * hzn ** 3 - 4.01 * hzn ** 2 + 2.25:.7g}'))
        r2 = str(float(f'{1.02 * hzn ** 2 - 0.95 * sin(5.2 * hzn) + 0.57:.7g}'))

        # Проверка на отрицательность значения r2
        if float(r2)<0:
            r2_sum+=float(r2)

        stroka = ('|' + ' ' *((max_len+8)//2 - len(h0)//2) + h0 +
                  ' '*(max_len + 8 - (max_len + 8)//2 - (len(h0)-len(h0)//2)) +
                  '|' + ' ' * ((max_len + 8) // 2 - len(r1) // 2) + r1 +
                  ' ' * (max_len + 8 - (max_len + 8) // 2 - (len(r1) - len(r1) // 2)) +
                  '|' + ' ' * ((max_len + 8) // 2 - len(r2) // 2) + r2 +
                  ' ' * (max_len + 8 - (max_len + 8) // 2
                            - (len(r2) - len(r2) // 2)) + '|')
        print(stroka)
        iterator+=h

    print(upper)
    print("Cумма отрицательных значений r2 (доп задание): " + str(r2_sum))
    # Длинна оси ординат
    len_ord = 120

    #Количество знакомест
    f_interv = (max_f - min_f)/(len_ord-1)

    # Приглашение на ввод количества засечек + проверка на верное количество
    inter_ct = int(input("Введите количество засечек (от 4 до 8): "))

    # Здесь будет храниться число использованных засечек
    isp_zas = 0

    #Берём данную переменную, чтобы ограничить число зачесек в строке 3-мя
    end_str = 0

    # Проверка данных
    if inter_ct < 4 or inter_ct > 8:
        print("Ошибка - невозможное количество засечек")

    else:
        # Интервал одной засечки
        zas_inter = (max_f - min_f) / (inter_ct - 1)

        #Создание границ засечки
        left_gr = min_f
        right_gr = left_gr + f_interv

        # Формирование строки интервала
        stroke = " " * max_lenh + " "
        low_chert = "-"*(max_lenh)

        # Кол-во засечек
        n_zas = 0

        # Создаём строку с засечками
        for k in range(len_ord):
            is_this_int = False
            is_this_len = 0

            # Перебираем значения засечек и ищем подходящую
            for i in range(isp_zas, inter_ct + 1):
                cut_zn = min_f + zas_inter * i

                # Если нашли подходящую - добавляем в строку
                if ((cut_zn >= left_gr or abs(left_gr - cut_zn) < eps) and
                        (cut_zn < right_gr)):
                    stroke += str(f"{cut_zn:.7g}")
                    low_chert += int(len(str(f"{cut_zn:.7g}"))/2)*'-' + '|' + '-'*int(len(str(f"{cut_zn:.7g}"))/2)
                    is_this_int = True
                    is_this_len = len(str(f"{cut_zn:.7g}"))
                    n_zas += 1
                    isp_zas += 1
                    end_str += len(str(f"{cut_zn:.7g}"))
                    break

            # Изменяем интервал
            if is_this_int is True:

                left_gr += f_interv * is_this_len
                right_gr += f_interv * is_this_len

            else:
                left_gr += f_interv
                right_gr += f_interv
                stroke += " "
                low_chert+="-"
                end_str += 1

            if end_str  > len_ord:
                break

        print(stroke)
        print(low_chert)
    # Интервалы для определения позиций точек
    f_interv = (max_f - min_f) / (len_ord-1)

    # Создаём итератор
    iterator = t_min

    # Переменная, хранящая количество иттераций цикла
    iterations = int(ceil((((t_max + h + eps) - t_min) // h)))

    # Построние границ графика
    for i in range(iterations):
        if abs(iterator)<eps:
            znach = '0'
        else:
            znach = str(float(f"{iterator:.7g}"))
        if iterator == t_min:
            r1 = min_f
        else:
            ct_z = iterator*pr
            r1 = 0.987 * ct_z ** 3 - 4.01 * ct_z ** 2 + 2.25

        stroka = ""

        # Добавление столбика со значением i
        stroka += (znach + " " * (max_lenh - len(znach)) + "|")

        # Значение позиций
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
            elif ((0 >= left_gr*pr) and
                    (0 < right_gr)):
                stroka += "|"

            # В иных случаях пропускаем данное значение
            else:
                stroka += " "

            left_gr += f_interv
            right_gr += f_interv

        print(stroka)

        iterator += h