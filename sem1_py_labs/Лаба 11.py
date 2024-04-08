# Пресняков А.К. ИУ7-13Б. Лабороторная работа 11
# Написать программу для демонстрации работы метода сортировки (по варианту) на
# примере массива целых чисел.
# Программа должна состоять из двух частей (этапов работы) и выполнять два действия
# последовательно:
# 1. сначала отсортировать заданный пользователем массив для доказательства
# корректности работы алгоритма;
# 2. затем составить таблицу замеров времени сортировки списков трёх различных
# (заданных пользователем) размерностей и количества перестановок в каждом
# из них

from random import *
from time import *

# Функция сортировки вставками с баьером
def barier_insertion_sort(list1):
    start_time = time()
    cnt = 0
    for i in range(1,len(list1)):
        value = list1[i]
        j = i - 1
        while value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
            cnt+=1
        list1[j + 1] = value
    delta_time = time() - start_time
    return list1, float("{:.7g}".format(delta_time)), cnt

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

# Функция ввода числа пользователем
def user_int_input():
    while True:
        try:
            N = int(input())
        except ValueError:
            print("Необходимо ввести число, попробуйте ещё раз")
        else:
            break
    return N

# Функция генерации массива случайных чисел с заданной рамзерностью
def random_list(N):
    list1 = [randint(1, 1000) for _ in range(N)]
    return list1

# Функция генерации сортированного массива случайных чисел с заданной рамзерностью
def sorted_list(N):
    list1 = random_list(N)
    list1.sort()
    return list1

# Функция генерации обратно сортированного массива случайных чисел с заданной рамзерностью
def reverse_sorted_list(N):
    list1 = random_list(N)
    list1.sort(reverse = True)
    return list1

# Функция построения таблицы
def table_build(len_total, len_first, len_N, len_t, len_k):
    print("-" * len_total)
    print("|" + " " * len_first + "|" + " " * (len_N // 2 - 1) + \
          "N1" + " " * (len_N // 2 - 1) + "|" + " " * (len_N // 2 - 1) + "N2" + \
          " " * (len_N // 2 - 1) + "|" + " " * (len_N // 2 - 1) + "N3" + \
          " " * (len_N // 2 - 1) + "|")
    print("-" * len_total)
    print("|" + " " * len_first + "|" + "    время    " + "|" + " перестановки " + \
          "|" + "    время    " + "|" + " перестановки " + "|" + "    время    " + "|" + " перестановки " + "|")
    print("-" * len_total)
    print("|" + " Упорядоченный " + "|" + str(t1) + " " * (len_t - len(str(t1))) \
          + "|" + str(k1) + " " * (len_k - len(str(k1))) + "|" \
          + str(t2) + " " * (len_t - len(str(t2))) + "|" \
          + str(k2) + " " * (len_k - len(str(k2))) + "|" \
          + str(t3) + " " * (len_t - len(str(t3))) + "|" \
          + str(k3) + " " * (len_k - len(str(k3))) + "|")
    print("-" * len_total)
    print("|" + "   Случайный   " + "|" + str(t4) + " " * (len_t - len(str(t4))) \
          + "|" + str(k4) + " " * (len_k - len(str(k4))) + "|" \
          + str(t5) + " " * (len_t - len(str(t5))) + "|" \
          + str(k5) + " " * (len_k - len(str(k5))) + "|" \
          + str(t6) + " " * (len_t - len(str(t6))) + "|" \
          + str(k6) + " " * (len_k - len(str(k6))) + "|")
    print("-" * len_total)
    print("|" + "   Обратный    " + "|" + str(t7) + " " * (len_t - len(str(t7))) \
          + "|" + str(k7) + " " * (len_k - len(str(k7))) + "|" \
          + str(t8) + " " * (len_t - len(str(t8))) + "|" \
          + str(k8) + " " * (len_k - len(str(k8))) + "|" \
          + str(t9) + " " * (len_t - len(str(t9))) + "|" \
          + str(k9) + " " * (len_k - len(str(k9))) + "|")
    print("-" * len_total)




# 1 ЧАСТЬ
# Вввод массива пользователем + вывод отсортированного массива
a = arrange_input()
a, t, k = barier_insertion_sort(a)
print("Отсортированный список: " + str(a))

# 2 ЧАСТЬ
# Ввод размерностей пользователем
print("Введите размерность N1: ", end ='')
N1 = user_int_input()
print("Введите размерность N2: ", end ='')
N2 = user_int_input()
print("Введите размерность N3: ", end ='')
N3 = user_int_input()

# СОЗДАНИЕ СПИСКОВ И ИХ ПАРАМЕТРОВ
# Сортированные
sorted_1 = sorted_list(N1)
sorted_2 = sorted_list(N2)
sorted_3 = sorted_list(N3)
sorted_1, t1, k1 = barier_insertion_sort(sorted_1)
sorted_2, t2, k2 = barier_insertion_sort(sorted_2)
sorted_3, t3, k3 = barier_insertion_sort(sorted_3)

# Случайные списки
random_1 = random_list(N1)
random_2 = random_list(N2)
random_3 = random_list(N3)
random_1, t4, k4 = barier_insertion_sort(random_1)
random_2, t5, k5 = barier_insertion_sort(random_2)
random_3, t6, k6 = barier_insertion_sort(random_3)


# Списки в обратном порядке
reverse_1 = reverse_sorted_list(N1)
reverse_2 = reverse_sorted_list(N2)
reverse_3 = reverse_sorted_list(N3)
reverse_1, t7, k7 = barier_insertion_sort(reverse_1)
reverse_2, t8, k8 = barier_insertion_sort(reverse_2)
reverse_3, t9, k9 = barier_insertion_sort(reverse_3)


# Создание таблицы
len_total = 104
len_first = 15
len_N = 28
len_t = 13
len_k = 14
table_build(len_total, len_first, len_N, len_t, len_k)