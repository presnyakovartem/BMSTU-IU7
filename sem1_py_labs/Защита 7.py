# Ввод количества элементов
n = int(input('Введите количество элементов списка: '))

# Проверка корректности ввода
if n < 1:
    print('Неправильный ввод количества элементов')

else:
    # Ввод списка
    a = [int(input('Введите ' + 'число '  + str(i+1) + ': ')) for i in range(n)]

    # Создаём индексы цепочек простых элементов
    from_index = to_index = None

    for i in range(len(a)):

        # Проверка на простоту
        is_Prime = True

        # Перебираем до корня, чтобы затратить меньше памяти
        for j in range(2, int(abs(a[i]) ** 0.5) + 1):

            if abs(a[i]) % j == 0:
                is_Prime = False

        if is_Prime is True:

            if from_index is None:
                from_index = i

            to_index = i

        elif from_index is not None:

            # Меняем позиции положительных и отрицательных
            a[i], a[from_index] = a[from_index], a[i]

            # Если в цепочке только один,элемент присваиваем ему индекс
            if to_index - from_index == 0:
                from_index = i

            else:
                from_index += 1

    a = a[:from_index]

    print(a)