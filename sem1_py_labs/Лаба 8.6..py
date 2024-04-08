# Пресняков А.К. ИУ7-13Б.Лабараторная 8.6.
# Вывод транспонированной матрицы

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

# Транспонирование
for s in range(n):
    for col in range(s+1,n):
        matrix[s][col], matrix[col][s] = matrix[col][s], matrix[s][col]

# Транспонированнй вывод
print("Итоговая матрица:")
for i in range(n):
    stroke = ''
    for j in range(n):
        step = 6
        element = f'{matrix[i][j]:.7g}'
        stroke += " " * step + element + " " * (12 - step - len(element))
    print(stroke)