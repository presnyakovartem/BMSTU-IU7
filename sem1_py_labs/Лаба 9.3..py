# Пресняков А.К ИУ7-13Б. Лаба 9.3.
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G

# Проверка корректности ввода
is_Correct = True
while is_Correct is True:

    # Ввод параметров матрицы
    n = int(input("Введите количество строчек матрицы D и Z: "))
    m = int(input("Введите количество столбцов матрицы D: "))
    m1 = int(input("Введите количество столбцов матрицы Z: "))
    matrix_d = []
    matrix_z = []

    if n < 1 and m < 1 and m1 < 1:
        print('Неправильный ввод размеров матриц')

    else:
        is_Correct = False

# Ввод матрицы D
for i in range(n):
    matrix_d.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + " матрицы D: ")) for j in range(m)])

# Ввод матрицы Z
for i in range(n):
    matrix_z.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + " матрицы Z: ")) for j in range(m1)])

# Вывод матрицы Z
print('Матрица Z')
for i in range(len(matrix_z)):
    stroke = ''

    for j in range(len(matrix_z[0])):
        element = '{:.7g}'.format(matrix_z[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

# Вывод матрицы D до
print('Матрица D до преобразований')
for i in range(len(matrix_d)):
    stroke = ''

    for j in range(len(matrix_d[0])):
        element = '{:.7g}'.format(matrix_d[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

# Создаём массив G
G = []

# Заполняем
for i in range(n):
    cnt = 0
    sum_stroke = 0
    for k in range(m1):
        sum_stroke += matrix_z[i][k]

    for j in range(m):
        if matrix_d[i][j] > sum_stroke:
            cnt+=1
    G.append(cnt)

# Вывод массива G
print(G)

# Находим макс элемент массива
max_g = max(G)

# Преобразуем матрицу D
for i in range(n):
    for j in range(m):
        matrix_d[i][j] = matrix_d[i][j] * max_g

# Второй вывод матрицы D
print('Матрица D после преобразований')
for i in range(len(matrix_d)):
    stroke = ''

    for j in range(len(matrix_d[0])):
        element = '{:.7g}'.format(matrix_d[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)