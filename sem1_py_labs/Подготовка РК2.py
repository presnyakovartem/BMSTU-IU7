1.1
a = [int(x) for x in input().split()]
a.sort()
b = [int(x) for x in input().split()]
b.sort()
c = []

index_a = 0
index_b = 0

while index_a < len(a) and index_b < len(b):
    if a[index_a] < b[index_b]:
        c.append(a[index_a])
        index_a+=1
    else:
        c.append(b[index_b])
        index_b+=1

while index_a < len(a):
    c.append(a[index_a])
    index_a+=1

while index_b < len(b):
    c.append(b[index_b])
    index_b+=1

print(c)


1.2
a = [int(x) for x in input().split()]
for i in range(len(a)):
    if a.count(a[i]) > 1:
        print('Некорректный ввод массива А')
        exit()

b = [int(x) for x in input().split()]
for i in range(len(b)):
    if b.count(b[i]) > 1:
        print('Некорректный ввод массива А')
        exit()

c = a

for i in range(len(b)):
    if c.count(b[i]) == 0:
        c.append(b[i])

print(c)


n = int(input("Введите количество строчек матрицы А: "))
m = int(input("Введите количество столбцов матрицы А и количество строчек матрицы B: "))
matrix_a = []
if n < 2 or m < 2:
    print("Некорректный ввод параметром матрицы А")
    exit()

for i in range(n):
    matrix_a.append([int(input("Введите элемент строки "\
    + str(i+1) + " стоблца " + str(j+1) + ": ")) for j in range(m)])

k = int(input("Введите количество столбцов матрицы B: "))
matrix_b = []

if k < 2:
    print("Некорректный ввод параметров матрицы B")
    exit()

for i in range(m):
    matrix_b.append([int(input(" Введите элемент " + str(i+1) + " строки " + str(j+1) + \
     " столбца:")) for j in range(k)])

# Инвертируем строчку для поворота на 90 по часовой
for line in range(len(matrix_b)):
  matrix_b[line] = matrix_b[line][::-1]

# Поворачиваем
for s in range(m):
    for col in range(m - s - 1, -1, -1):
        matrix_b[s][col], matrix_b[m - col - 1][m - s - 1] = matrix_b[m - col - 1][m - s - 1], matrix_b[s][col]

print("Итоговая матрица")
new_matrix = matrix_a + matrix_b
for i in range(len(new_matrix)):
    stroke = ''
    for j in range(len(new_matrix[0])):
        element = '{:.7g}'.format(new_matrix[i][j])
        cut = 6
        stroke += ' ' * cut + str(element) + ' ' * (12 - cut - len(str(element)))
    print(stroke)

line_sum = []

for i in range(len(new_matrix)):
    line_sum.append(sum(new_matrix[i]))

max_sum_cnt = float('-inf')
max_sum_index = None
for i in range(len(line_sum)):
    if line_sum.count(line_sum[i]) > max_sum_cnt:
        max_sum_cnt = line_sum.count(line_sum[i])
        max_sum_index = i


if max_sum_index is None:
    print('В матрице нет строк с одинаковой суммой')

else:
    print('Первая строка, с наибольшим количеством строк с одинаковой суммой элементов')
    print(new_matrix[max_sum_index])


