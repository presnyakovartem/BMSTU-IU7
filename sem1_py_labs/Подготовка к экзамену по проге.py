'''ЗАДАЧА 1 горизонтальная последовательность'''

matrix = [[1,2,"#","#",4], [3,"#","#","#",5], [1,2,3,"#",4], [1,6,"#","#",4], ["#",2,"#","#",4]]
m = len(matrix)
n = len(matrix[0])
max_len = float("-inf")
index_max = None
for i in range(m):
    max_count = 0
    if "#" not in matrix[i]:
        continue
    count = 1

    for j in range(n-1):

        if str(matrix[i][j]) == "#" and str(matrix[i][j+1]) == "#":
            count += 1
            max_count = max(count, max_count)
            max_len = max(max_len, max_count)

        elif str(matrix[i][j]) == "#" and str(matrix[i][j+1]) != "#":
            max_len =  max(max_len, max_count)
            count = 1
    if index_max is None:
        index_max = i

    elif max_count == max_len:
        index_max = i

indexes = []
count_resh = matrix[index_max].count("#")
for i in range(1, count_resh+1):
    if len(indexes) == 0:
        indexes.append(matrix[index_max].index("#", i))

    elif matrix[index_max].index("#", i) - matrix[index_max].index("#", i-1) == 1:
        indexes.append(matrix[index_max].index("#", i))

    else:
        indexes.clear()

cols_count = [0]*n
for i in indexes:
    count = 0

    for j in range(m):
        if matrix[j][i] == '#':
            count += 1
    cols_count[i] = count

cols_count1 = cols_count.copy()
matrix.append(cols_count1)
m = len(matrix)
print(matrix)
sort_indexes = []
for i in range(n):
    sort_indexes.append(cols_count.index(max(cols_count)))
    cols_count[cols_count.index(max(cols_count))] = -1
sorted_matrix = []

for i in range(m):
    line = []

    for j in range(n):
        line.append(matrix[i][sort_indexes[j]])
    sorted_matrix.append(line)
print(sorted_matrix)






''' ЗАДАЧА 2. СТРЕЛОЧНАЯ МАТРИЦA '''
#Функция для поиска последовательности начиная из произвольной клетки матрицы
def line_info(matrix, s, c, i, j, current_length, checked_points, column_count):

    # Проверка на отсутствие выхода за переделы
    if i < 0 or i == s or j < 0 or j == c or ([i,j] in checked_points):
        return [current_length, column_count,]

    else:
        current_length += 1
        column_count[j] += 1
        checked_points.append([i,j])

        # Рассматриваем каждый случай по отдельности и делаем рекурсию в случай если следующий символ не является членом последовательности
        if matrix[i][j] == '>':
            try:
                if matrix[i][j+1] == '<':
                    return [current_length, column_count, ]
            except Exception:
                return [current_length, column_count, ]

            return line_info(matrix, s, c, i, j+1, current_length, checked_points, column_count)

        elif matrix[i][j] == '<':
            try:
                if matrix[i][j - 1] == '>':
                    return [current_length, column_count, ]
            except Exception:
                return [current_length, column_count, ]

            return line_info(matrix, s, c, i, j-1, current_length, checked_points, column_count)

        elif matrix[i][j] == 'v':
            try:
                if matrix[i+1][j] == '^':
                    return [current_length, column_count, ]
            except Exception:
                return [current_length, column_count, ]

            return line_info(matrix, s, c, i+1, j, current_length, checked_points, column_count)

        elif matrix[i][j] == '^':
            try:
                if matrix[i-1][j] == 'v':
                    return [current_length, column_count, ]
            except Exception:
                return [current_length, column_count, ]

            return line_info(matrix, s, c, i-1, j, current_length, checked_points, column_count)

# Считывание матрицы
matrix = []
file1 = open("in.txt", "rt")
line = file1.readline()

# Удаление лишних символов
line = line.rstrip()

line = line.split()
matrix.append(line)
s = 1
c = len(matrix[0])
while (line := file1.readline()) != '':
    line = line.rstrip()
    line = line.split()
    matrix.append(line)
    s+=1
for i in matrix:
    print(i)

# Переменная бдет содержать себе информацию о текущей длинне последвоательность и количестве символов последовательности для столбцов
max_length = [0,0]

# Поиск по всем клеточкам
for i in range(s):
    for j in range(c):
        line_inf = line_info(matrix, s, c, i, j, 0, [], [0 for _ in range(c)])
        print(line_inf)
        max_length = max(line_inf, max_length, key = lambda x: x[0])

# Сортировка индексов столбцов по последней строке
max_length = max_length[1]
column_count = max_length.copy()
column_count_indexes = []
for i in range(c):
    column_count_indexes.append(column_count.index(max(column_count)))
    column_count[column_count.index(max(column_count))] = -1
column_count_indexes.sort(reverse = True)
sorted_matrix = []

# Добавление новой строки в конец матрицы
matrix.append(max_length)
for i in matrix:
    print(i)

# Создание отсортированной матрицы
for i in range(s+1):
    line = []
    for j in range(c):
        line.append(matrix[i][column_count_indexes[j]])
    sorted_matrix.append(line)

for i in sorted_matrix:
    print(i)

with open ("out.txt", "wt") as file2:
    for i in sorted_matrix:
        line = ''
        for j in i:
            line += (str(j) + ' ')
        line.removesuffix(' ')
        line+="\n"
        file2.write(line)




''' ЗАДАЧА 3. ПОВОРОТ КОНТУРОВ МАТРИЦЫ '''
def rotate_forhour(matrix, n, i):
    for line in range(i,n+i):
        matrix[line][i:n+i] = reversed(matrix[line][i:n+i])
    for s in range(i, n+i):
        for c in range(n - s - 1 + i, -1 + i, -1):
            matrix[s][c], matrix[n - c - 1 + i][n - s - 1 + i] = matrix[n - c - 1 + i][n - s - 1 + i], matrix[s][c]
    return matrix

def rotate_uponhour(matrix, n, i):
    for s in range(i, n+i):
        for c in range(n - s - 1 + i, -1 + i, -1):
            matrix[s][c], matrix[n - c - 1 + i][n - s - 1 + i] = matrix[n - c - 1 + i][n - s - 1 + i], matrix[s][c]
    for line in range(i, n+i):
        matrix[line][i:n+i] = reversed(matrix[line][i:n+i])
    return matrix

matrix = []
file1 = open("in1.txt", "rt")
line = file1.readline()

# Удаление лишних символов
line = line.rstrip()

line = line.split()
matrix.append(line)
c = len(matrix[0])
while (line := file1.readline()) != '':
    line = line.rstrip()
    line = line.split()
    matrix.append(line)
for i in matrix:
    print(i)

count = 1
for i in range(c//2):
    if c%2 != 0:
        if count % 2 != 0:
            for j in range(count):
                matrix = rotate_forhour(matrix, c - i * 2, i)
                count+=1
                print()
                for k in matrix:
                    print(k)
        else:
            for j in range(count):
                matrix = rotate_uponhour(matrix, c - i * 2, i)
                count += 1
                print()
                for k in matrix:
                    print(k)



'''ЗАДАЧА 4 ДИАГОНАЛИ ПРОЦЕНТОВ'''
def prepare_stroke(stroke, arrange):
    v = 0
    check_stroke = stroke
    check_arrange = arrange
    for i in range(len(check_stroke)):
        if check_arrange[i] == 2:
            check_stroke = check_stroke[:i - v] + check_stroke[i + 1 - v:]
            v+=1
    return check_stroke

def pallindrom_count(stroke):
    c = 0
    for i in range(len(stroke) - 1):
        for j in range(i + 1, len(stroke)):
            check = stroke[i:j+1]
            if check == check[::-1]:
                c+=1
    return c

out  = open("out2.txt", "wt")
with open("in2.txt", "rt") as infile:
    stroke_last = infile.readline()
    if stroke_last == '':
        print("Файл пуст")
    else:
        stroke_last = stroke_last.rstrip()
        arrange_last = [0]*100
        for i in range(len(stroke_last)):
            if stroke_last[i] == "%":
                arrange_last[i]+=1

        while (stroke:=infile.readline()) != '':
            stroke = stroke.rstrip()
            arrange = [0]*100
            for i in range(len(stroke)):
                if stroke[i] == '%':
                    if i == 0:
                        arrange[i] = 1
                    elif i == 99:
                        arrange[i] = 2
                    elif arrange_last[i-1] == 1 or arrange_last[i-1] == 2:
                        arrange[i] = 2
                        arrange_last[i-1] = 2
                    else:
                        arrange[i] = 1
            stroke_ready = prepare_stroke(stroke_last,arrange_last)
            out.write(stroke_ready +  f" {pallindrom_count(stroke_last)}" + "\n")
            stroke_last = stroke
            arrange_last = arrange
    stroke_ready = prepare_stroke(stroke_last, arrange_last)
    out.write(stroke_ready + f" {pallindrom_count(stroke_last)}" + "\n")

out.close()






