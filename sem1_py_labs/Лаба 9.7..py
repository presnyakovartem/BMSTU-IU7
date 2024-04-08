# Пресняков А.К. ИУ7-13Б. Лабораторная 9.7.
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
# индексов начинается с 1). NumPy не использовать



# Ввод параметров
X = int(input("Введите количество матриц внутри массива: "))
Y = int(input("Введите количество строчек матриц: "))
Z = int(input("Введите количество столбцов матриц: "))

# Создаем трёхмерный массив
array_3d = [[[int(input("Введите \
элемент столбца " + str(j+1) + " строки\
 " + str(k+1) + " массива " + str(i+1) + ": ")) for j in range(X)]\
for k in range(Y)] for i in range(Z)]

# Ввод индекса среза
is_Correct_Input = True
while is_Correct_Input:
    I = int(input("Введите номер среза: "))
    if I > Y:
        print("неправильна")
    else:
        is_Correct_Input = False

# Определение среза
cut = [array_3d[k][I-1] for k in range(len(array_3d))]

# Вывод среза
print('i-й срез')
for i in range(len(cut)):
    stroke = ''

    for j in range(len(cut[0])):
        element = '{:.7g}'.format(cut[i][j])
        step = 6
        stroke += ' ' * step + str(element) + ' ' * (12 - step - len(str(element)))

    print(stroke)