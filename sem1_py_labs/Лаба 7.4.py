# Пресняков Артём ИУ7-13Б. Лаба 7.1
# Поиск более короткого элемента без пробелов

# Ввод количества элементов
n = int(input('Введите количество элементов списка: '))

# Проверка корректности ввода
if n < 1:
    print('Неправильный ввод количества элементов')

else:
    # Ввод списка
    a = [str(input('Введите ' + 'строку '  + str(i+1) + ': ')) for i in range(n)]

    # Создадим список цифр
    integers = ['1','2','3','4','5','6','7','8','9']

    # Произведём перебор для поиска элементов и последующей замены
    for i in range(len(a)):

        for j in integers:
            string_edit  = a[i].replace(j, ' ')
            a[i] = string_edit

    # Вывод
    stroke = ''
    for i in range(len(a)):

        if i+1 == len(a):
            stroke += str(a[i])

        else:
            stroke += str(a[i]) + ', '

    print(stroke)
