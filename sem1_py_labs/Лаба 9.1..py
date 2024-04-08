# Пресняков А.К. ИУ7-13Б.Лабараторная 9.1.
# Даны массивы D и F. Сформировать матрицу A по формуле
# ajk = sin(dj+fk)
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и массивы AV и L.

from math import *


# Проверка корректности ввода
is_Correct = True
while is_Correct is True:

    # Ввод количества элементов
    j = int(input('Введите количество элементов массива D: '))

    if j < 1:
        print('Неправильный ввод количества элементов')

    else:
        is_Correct = False

# Ввод списка
    D = [int(input('Введите ' + 'число '  + str(i+1) + ' массива D: ')) for i in range(j)]

# Проверка корректности ввода
is_Correct = True
while is_Correct is True:

    # Ввод количества элементов
    k = int(input('Введите количество элементов массива F: '))

    if k < 1:
        print('Неправильный ввод количества элементов')

    else:
        is_Correct = False

    # Ввод списка
    F = [int(input('Введите ' + 'число '  + str(i+1) + ' массива F: ')) for i in range(k)]

# Создание матрицы
matrix_a = [0]*j
for i in range(j):
    stroke = []
    for z in range(k):
        element = sin(D[i] + F[z])
        stroke.append(float('{:.7g}'.format(element)))
    matrix_a[i] = stroke

# Создание массивов для хранения сред. афм и кол-во элементов строки
AV = []
L = []
for i in range(j):
    sum_plus = 0
    cnt_plus = 0
    has_plus = False

    for j in range(k):

        if matrix_a[i][j] > 0:
            has_plus = True
            sum_plus += matrix_a[i][j]
            cnt_plus += 1

    if has_plus is True:
        average_sum = sum_plus / cnt_plus
        AV.append(average_sum)
        for z in range(k):
            if matrix_a[i][z] < average_sum:
                L.append(matrix_a[i][z])

    else:
        AV.append('none')

# Вывод
print('Итоговая матрица')
for i in range(len(matrix_a)):
    stroke = ''
    for j in range(len(matrix_a[0])):
        element = '{:.7g}'.format(matrix_a[i][j])
        cut = 10
        stroke += ' ' * cut + str(element) + ' ' * (20 - cut - len(str(element)))
    print(stroke)

print()
print("Массив AV")
for i in range(len(AV)):
    print(AV[i])
print()
print("Массив L")
for i in range(len(L)):
    print(L[i])