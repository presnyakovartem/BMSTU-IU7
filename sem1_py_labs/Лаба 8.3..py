# Пресняков А.К. ИУ7-13Б.Лабараторная 8.3
# Найти столбец имеющий наибольшее количество элементов являющимися степенью двойки

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

# Создаём наибольшее количество и индекс стоблца
max_two_elements = float('-inf')
index_max = None

for i in range(m):
    two_count = 0

    for j in range(n):

        # Проверка на то, является ли элемент степенью двойки
        two_step = matrix[j][i]
        while two_step > 1:
            two_step //= 2

        if two_step == 1:
            two_count+=1

    if two_count > max_two_elements and two_count != 0:
        max_two_elements = two_count
        index_max = i

if index_max is None:
    print('В матрице нет элемента, являющегося степенью двойки')

else:
    for i in range(m):
        print(matrix[i][index_max])
