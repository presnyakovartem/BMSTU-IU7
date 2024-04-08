# Пресняков А.К. ИУ7-13Б.Лабараторная 8.4.
# Переставить местами столбцы с максимальной и минимальной суммой
# элементов.

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

# Создаёи переменные, для хранения информации о сумме элементов столбца
min_sum_elements = float('inf')
max_sum_elements = float('-inf')
index_max = None
index_min = None

for i in range(m):

    # Переменная, хранящая количество отриц. элементов в строке
    sum_cur = 0

    for j in range(n):

        sum_cur += matrix[j][i]

    # Сравнение с максимальным количеством
    if sum_cur > max_sum_elements:
        max_sum_elements = sum_cur
        index_max = i

    # Сравнение с минимальным количеством
    if sum_cur < min_sum_elements:
        min_sum_elements = sum_cur
        index_min = i

for i in range(n):
    matrix[i][index_min], matrix[i][index_max] = matrix[i][index_max],\
    matrix[i][index_min]

# Вывод
print("Итоговая матрица:")
for line in matrix:
    stroke = ""
    for col in line:
        element = f"{col:.7g}"
        step = 6
        stroke += " " * step + element + " " * (12 - step - len(element))
    print(stroke)

