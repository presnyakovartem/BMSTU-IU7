# Пресняков А.К. ИУ7-13Б. Лабораторная 9.6
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.


# Проверка корректности ввода + ввод параметров
is_Correct = True
while is_Correct is True:

    # Ввод параметров матрицы
    n = int(input("Введите количество строчек матрицы A и B: "))
    m = int(input("Введите количество столбцов матрицы А и В: "))
    matrix_a = []
    matrix_b = []

    if n < 1 and m < 1:
        print('Неправильный ввод размеров матриц')

    else:
        is_Correct = False

# Ввод матрицы A
for i in range(n):
    matrix_a.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + " матрицы А: ")) for j in range(m)])

# Ввод матрицы B
for i in range(n):
    matrix_b.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + " матрицы B: ")) for j in range(m)])

# Создаём матрицу C и массив V
C = []
V = []
for i in range(n):
    current_line = []
    for j in range(m):
        current_line.append(matrix_a[i][j] * matrix_b[i][j])
    C.append(current_line)
    V.append(sum(C[i]))

# Вывод
# Матрица A
print('Матрица A')
for i in range(len(matrix_a)):
    stroke = ''

    for j in range(len(matrix_a[0])):
        element = '{:.7g}'.format(matrix_a[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

# Матрица B
print('Матрица B')
for i in range(len(matrix_b)):
    stroke = ''

    for j in range(len(matrix_b[0])):
        element = '{:.7g}'.format(matrix_b[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

# Матрица C
print('Матрица C')
for i in range(len(C)):
    stroke = ''

    for j in range(len(C[0])):
        element = '{:.7g}'.format(C[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

# Массив V
print("Массив V")
print(V)