def bubble_sort(list1):
    is_Sorted =  True
    for i in range(len(list1)-1):
        for j in range(len(list1) - i - 1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                is_Sorted = False
        if is_Sorted:
             break
        else:
            is_Sorted = True
    return list1

# Функция ввода списка пользователем
def arrange_input():
    while True:
        try:
            list1 = list( map(int,input("Введите элементы массива через пробел: ").split()) )
        except ValueError:
            print("Массив может содержать только числа")
        else:
            break
    return list1

a = arrange_input()
a= bubble_sort(a)
print("Отсортированный список: " + str(a))