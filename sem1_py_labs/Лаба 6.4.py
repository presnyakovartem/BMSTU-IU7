# Пресняков Артём ИУ7-13Б. Лабороторная 6.4.9
# Найти наиболее длинную непрерывную последовательность по варианту
# Убывающая последовательность отрицательных чисел, модуль которых
# является простым числом.


# Ввод количества элементов
n = int(input('Введите количество элементов списка: '))

# Проверка корректности ввода
if n < 1:
    print('Неправильный ввод количества элементов')

else:
    # Ввод списка
    a = [int(input('Введите ' + 'элемент '  + str(i+1) + ': ')) for i in range(n)]

    # Поиск длины самой длинной последовательность
    b_cur = []
    b_max = []
    for i in range(len(a)):
        is_Prime = True

        for j in range(2, int(abs(a[i]) ** 0.5) + 1):

            if abs(a[i]) % j == 0:
                is_Prime = False

        if is_Prime is False or a[i] >= 0:

            if len(b_cur) > len(b_max):
                b_max = b_cur

            b_cur = []

        elif a[i] < 0 and is_Prime is True:

            if len(b_cur) == 0:
                b_cur.append(a[i])

            elif b_cur[-1] < a[i]:
                b_cur = [a[i]]

            elif b_cur[-1] > a[i]:
                b_cur.append(a[i])

    if len(b_cur) > len(b_max):
        b_max = b_cur

    if len(b_max) == 0:
        print('Нет такого ряда')
        exit()

    # Вывод
    stroke = ''
    for i in range(len(b_max)):

        if i+1 == len(b_max):

            stroke += str(b_max[i])

        else:

            stroke += str(b_max[i]) + ', '

    print(stroke)
