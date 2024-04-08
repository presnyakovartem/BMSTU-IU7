# Пресняков А.К. ИУ7-13Б. Лабороторная 9.5
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования. Python

# Проверка корректности ввода + ввод параметров
is_Correct = True
while is_Correct is True:

    # Ввод параметров матрицы
    n = int(input("Введите количество строчек матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    matrix_d = []

    if n < 1 and m < 1:
        print('Неправильный ввод размеров матриц')

    else:
        is_Correct = False

# Ввод матрицы
for i in range(n):
    matrix_d.append([str(input("Введите строку строки "\
    + str(i+1) + " стоблца " + str(j+1) + ": ")) for j in range(m)])

# Вывод первоначальной матрицы
print('Матрица до преобразований')
for i in range(len(matrix_d)):
    stroke = ''

    for j in range(len(matrix_d[0])):
        element = matrix_d[i][j]
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

# Создаём алфавит
vowels = 'aeiouyAEIOUY'

# Замена через перебор
for i in range(n):
    for j in range(m):
        for l in vowels:
            if l in matrix_d[i][j]:
                matrix_d[i][j] = matrix_d[i][j].replace(l,".")

# Вывод конечной матрицы
print('Матрица после преобразований')
for i in range(len(matrix_d)):
    stroke = ''

    for j in range(len(matrix_d[0])):
        element = matrix_d[i][j]
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

