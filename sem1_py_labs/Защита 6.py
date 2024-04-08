# Ввод количества элементов
n = int(input('Введите количество элементов списка: '))

# Проверка корректности ввода
if n < 1:
    print('Неправильный ввод количества элементов')

else:
    # Ввод списка
    a = [int(input('Введите ' + 'элемент '  + str(i+1) + ': ')) for i in range(n)]

    # Находим значение минимального
    a_min = min(a)

    # Находим значение минимального
    a_max = max(a)

    # Зададим индекс мин элемента
    a_min_f_index = None

    # Зададим индекс макс элемента
    a_max_l_index = None

    for i in range(len(a)):

        if a[i] == a_min:

            if a_min_f_index is None:
                a_min_f_index = i

        if a[i] == a_max:
            a_max_l_index = i

    a[a_max_l_index] = a_min
    a[a_min_f_index] = a_max

    print(a)
