# Пресняков А.К. ИУ7-13Б.Лабараторная 8.5.
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю

# Ввод параметров матрицы
n = int(input("Введите размер квадратной матрицы: "))

# Проверка
if n < 2:
    print("Некорректный ввод размера матрицы")
    exit()

# Ввод матрицы
matrix = []
for i in range(n):
    matrix.append([int(input("Введите элемент строки "
    + str(i+1) + " стоблца " + str(j+1) + ": ")) for j in range(n)])

# Переменные, для хранения макс и мин значений
max_element = float('-inf')
min_element = float('inf')

# Проход над верхней диагональю
for i in range(n):

    for j in range(i+1,n):

        if matrix[i][j] > max_element:
            max_element = matrix[i][j]

# Проход под побочной диагональю
for i in range(1,n):

    for j in range(n-i,n):

        if matrix[i][j] < min_element:
            min_element = matrix[i][j]

# Вывод
print(max_element,min_element)