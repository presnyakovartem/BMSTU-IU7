# Пресняков Артём ИУ7-13Б. Лаба 7.1
# Добавить после отриц. элемента его удвоенное значения

# Ввод количества элементов
n = int(input('Введите количество элементов списка: '))

# Проверка корректности ввода
if n < 1:
    print('Неправильный ввод количества элементов')

else:
    # Ввод списка
    a = [int(input('Введите ' + 'число '  + str(i+1) + ': ')) for i in range(n)]

    # Подсчитаем количество отриц элементов
    k_minus = 0
    for i in range(len(a)):

        if a[i] < 0:
            k_minus += 1

    # Создадим ячейки под удв значения
    a = [0] * k_minus + a

    # Индекс нового элмента
    current_index = 0

    # Производим замену
    for i in range(k_minus, len(a)):

        a[current_index] = a[i]

        if a[current_index] < 0:
            a[current_index+1] = a[current_index] * 2

            current_index += 1

        current_index += 1

    # Вывод
    stroke = ''
    for i in range(len(a)):

        if i + 1 == len(a):
            stroke += str(a[i])

        else:
            stroke += str(a[i]) + ', '

    print(stroke)