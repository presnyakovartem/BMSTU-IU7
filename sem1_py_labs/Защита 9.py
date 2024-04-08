# Проверка корректности ввода
is_Correct_Input = False
while not(is_Correct_Input):

    # Ввод параметров
    n = int(input('Введите количество строчек матрицы: '))
    m = int(input('Введите количество столбцов матрицы: '))

    if n < 2 or m < 2:
        print('Неправильный ввод параметров матрицы')

    else:
        is_Correct_Input = True

# Ввод матрицы
matrix_a = []

for i in range(n):
        matrix_a.append([int(input("Введите элемент строки "\
        + str(i+1) + " стоблца " + str(j+1) + ": ")) for j in range(m)])

# Создание подматрицы
min_element = float("inf")
min_element_index_1 = None
min_element_index_2 = None
max_element = float("-inf")
max_element_index_1 = None
max_element_index_2 = None
for i in range(n):

    for j in range(m):

        if matrix_a[i][j] > max_element:
            max_element = matrix_a[i][j]
            max_element_index_1 = i
            max_element_index_2 = j

        if matrix_a[i][j] < min_element:
            min_element = matrix_a[i][j]
            min_element_index_1 = i
            min_element_index_2 = j

print(min_element_index_1, min_element_index_2)
print(max_element_index_1, max_element_index_2)
# Исходная матрицы
print("Исходная матрица")
for i in range(len(matrix_a)):
    stroke = ''

    for j in range(len(matrix_a[0])):
        element = '{:.7g}'.format(matrix_a[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)
matrix_b = []
if 1 == 0:
    print("Элементы будут расположены не по диагонали")

else:
    for i in range(min_element_index_1, max_element_index_1 + 1):
        for j in range(min_element_index_2, max_element_index_2 + 1):
            matrix_b.append(matrix_a[i][j])


    # Подматрица
    print("Подматрица")
    for i in range(len(matrix_b)):
        stroke = ''

        for j in range(len(matrix_b[0])):
            element = '{:.7g}'.format(matrix_b[i][j])
            cut = 6
            stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

        print(stroke)

    # Подсчёт сред.арифм
    cnt_plus = 0
    sum_plus = 0
    for i in range(len(matrix_b)):

        for j in range(len(matrix_b[0])):

            if matrix_b[i][j] > 0:
                sum_plus += matrix_b[i][j]
                cnt_plus += 1

    if cnt_plus == 0:
        print("В подматрице нет положительных элементов")

    else:
        average_sum = str("{:.7g}".format(sum_plus / cnt_plus))
        print("Среднее арифметическое положительных элементов подматрицы: " + average_sum)
