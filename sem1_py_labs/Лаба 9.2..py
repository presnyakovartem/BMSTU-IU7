# Пресняков А.К. ИУ7-13Б. Лабораторная 9.2.
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.


# Проверка корректности ввода
is_Correct = True
while is_Correct is True:

    # Ввод параметров
    n = int(input('Введите размер квадратной матрицы: '))

    if n < 2:
        print('Неправильный ввод размера квадратной матрицы')

    else:
        is_Correct = False

# Ввод матрицы
matrix_a = []
for i in range(n):
    matrix_a.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + ": ")) for j in range(n)])

# Инвертируем строчку
for line in range(len(matrix_a)):
  matrix_a[line] = matrix_a[line][::-1]

# Поворачиваем
for s in range(n):

    for col in range(n - s - 1, -1, -1):
        matrix_a[s][col], matrix_a[n - col - 1][n - s - 1] = matrix_a[n - col - 1][n - s - 1], matrix_a[s][col]

# Промежуточный вывод
print('Промежуточная матрица')
for i in range(len(matrix_a)):
    stroke = ''

    for j in range(len(matrix_a[0])):
        element = '{:.7g}'.format(matrix_a[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

# Поворачиваем
for s in range(n):

    for col in range(n - s - 1, -1, -1):
        matrix_a[s][col], matrix_a[n - col - 1][n - s - 1] = matrix_a[n - col - 1][n - s - 1], matrix_a[s][col]

# Инвертируем строчку
for line in range(len(matrix_a)):
  matrix_a[line] = matrix_a[line][::-1]

# Итоговый вывод
print('Итоговая матрица')
for i in range(len(matrix_a)):
    stroke = ''

    for j in range(len(matrix_a[0])):
        element = '{:.7g}'.format(matrix_a[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)
