# Пресняков А.К. ИУ7-13Б.Лабараторная 8.2.
# Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов.

# Ввод параметров матрицы
n = int(input("Введите количество строчек матриц матрицы: "))
m = int(input("Введите количество столбцов матриц матрицы: "))

# Проверка
if n < 2 or m < 2:
    print("Некорректный ввод размера матрицы")
    exit()

# Ввод матрицы
matrix = []
for i in range(n):
    matrix.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + ": ")) for j in range(m)])

# Создаёи переменные, для хранения информации о количестве отрицательных
# элементов строках
min_minus_elements = float('inf')
max_minus_elements = float('-inf')
index_max = None
index_min = None

for i in range(n):

    # Переменная, хранящая количество отриц. элементов в строке
    minus_count = 0

    for j in range(m):

        if matrix[i][j] < 0:
            minus_count += 1

    # Сравнение с максимальным количеством
    if minus_count > max_minus_elements and minus_count != 0:
        max_minus_elements = minus_count
        index_max = i

    # Сравнение с минимальным количеством
    if minus_count < min_minus_elements and minus_count != 0:
        min_minus_elements = minus_count
        index_min = i

if index_min == None:
    print("В матрице нет отрицательных элементов")

else:
    matrix[index_min], matrix[index_max] = matrix[index_max], matrix[index_min]

    # Вывод
    print("Итоговая матрица:")
    for line in matrix:
        stroke = ""
        for col in line:
            element = f"{col:.7g}"
            step = 6
            stroke += " " * step + element + " " * (12 - step - len(element))
        print(stroke)

