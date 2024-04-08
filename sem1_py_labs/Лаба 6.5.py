# Пресняков Артём ИУ7-13Б. Лабороторная 6.5.10
# Поменять местами элементы с характеристиками по варианту
# Последний чётный и минимальный положительный.


# Ввод количества элементов
n = int(input('Введите количество элементов списка: '))

# Проверка корректности ввода
if n < 1:
    print('Неправильный ввод количества элементов')

else:
    # Ввод списка
    a = [int(input('Введите ' + 'элемент '  + str(i+1) + ': ')) for i in range(n)]

    # Создание переменных, хранящих значение индекса необходимых элементов
    # а также определяем мин элемент
    min_index = 0
    index_even = None

    # Счётчик положительных
    ct_plus = 0

    for i in range(len(a)):

        if a[i] > 0 and a[i] < a[min_index]:
            min_index = i

        if a[i] % 2 == 0:
            index_even = i

        if a[i] > 0:
            ct_plus+=1

    if index_even is None:
        print('Не существует чётного элемента списка')
        exit()

    if ct_plus == 0:
        print('Не существует положительных элементов')
        exit()

    min_element = a[min_index]
    even_element = a[index_even]
    a[even_element] = min_element
    a[min_element] = even_element

    # Вывод
    stroke = ''
    for i in range(len(a)):

        if a[i] == len(a):
            stroke += str(a[i])

        else:
            stroke += str(a[i]) + ', '

    print(stroke)