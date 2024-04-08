# Пресняков А.К. ИУ7-13Б. Лабороторная работа 9.4.
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.

# Проверка корректности ввода + ввод параметров
is_Correct = True
while is_Correct:

    # Ввод параметров матрицы
    n = int(input("Введите количество строчек матрицы D: "))
    m = int(input("Введите количество столбцов матрицы D: "))
    matrix_d = []

    if n < 1 and m < 1:
        print('Неправильный ввод размеров матриц')

    else:
        is_Correct = False

# Ввод матрицы
for i in range(n):
    matrix_d.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + ": ")) for j in range(m)])

# Ввод массива + проверка
is_Correct = False
while is_Correct is False:
    k = int(input("Введите количество строчек (не более чем, в матрице D)\
, в которых необходоим найти макс: "))
    I = [int(input('Введите ' + 'номер строчки '  + str(i+1) + ': ')) for i in range(k)]
    for i in range(k):
        if I.count(I[i]) != 1 or I[i] > n-1 or I[i] < 0:
            print("Некорректный ввод массива")
            is_Correct = False
        else:
            is_Correct = True
    if k > n:
        print("В матрице меньше строчек, чем значений в массиве")
        is_Correct = False

# Создаём массив R
R =[]
for i in range(n):
    if i in I:
        R.append(max(matrix_d[i]))

# Среднее арифметич
average_sum = '{:.7g}'.format(sum(R)/len(R))

# Вывод
# Матрица D
print('Матрица D')
for i in range(len(matrix_d)):
    stroke = ''

    for j in range(len(matrix_d[0])):
        element = '{:.7g}'.format(matrix_d[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))

    print(stroke)

#Массивы R и I + ср афм R
print("Массив I")
print(I)
print("Массив R")
print(R)
print("Среднее арифметическое R: " + str(average_sum))

