# Пресняков Артём ИУ7-13Б. Лабороторная 6.2б
# Удалить элемент из списка по индексу алгоритмически

# Ввод количества элементов списка
n = int(input('Введите количество элементов списка: '))

# Проверка корректности ввода
if n < 1:
    print('Неправильный ввод количества элементов')

else:

    #Ввод списка
    a = [int(input('Введите ' + 'элемент '  + str(i+1) + ': ')) for i in range(n)]

    # Ввод индекса элемента, который надо удалить
    index_el = int(input('Введите индекс элемента, \
который надо удалить (0 является первым): '))

    # Удаление
    for i in range(index_el, len(a)-1):
        a[i] =a[i+1]

    a.pop()

    # Вывод
    stroke = ''
    for i in range(len(a)):
        if a[i] == len(a):
            stroke += str(a[i])
        else:
            stroke += str(a[i]) + ', '

    print(stroke)