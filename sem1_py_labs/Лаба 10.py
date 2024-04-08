# Пресняков А.К. ИУ7-13Б. Лабороторная 10
# Вычисление приближённого значения интеграла двумя методами, вывод таблицей
# Найти аболсютную и относительную погрешность обоих методов, вывод таблицей
# Метод серединных прямоугольников + трапеций
# Для менее точного метода, итерационно вычислить количество участков
# разбиения, для которого интеграл будет вычислен с заданной пользователем точностью, на основе
# формулы:

# Функция для преобразования
def f(x):
   return (0.1 * (x**2)) + 1

# Первообразная
def F(x):
   return 1/30 * (x**3) + x

# Фунцкия подсчёта асболютной погрешности
def absolute_eps(i, i_real):
   if i == 'None' :
      return 'None'
   return abs(i - i_real)

# Функция подсчёта относительной погрешности
def relative_eps(absolute, i_real):
   if absolute == 'None':
      return 'None'
   return absolute / ((i_real * 100) + 1e-5)

# Проверка ввода. Является ли числом.
def is_iterable(iterable):

   # Переводим в строку для проверки
   check = str(iterable)
   count_sym = 0

   # Подсчитыаем число символов, возможных при вводе числа
   for num_strings in "0123456789e-.":
      count_sym += check.count(num_strings)

   if count_sym != len(check):
      return False

   # Проверка в случае степени
   if 'e' in check:
      if check.count('e') != 1 or check[0] == 'e' or check[-1] == 'e':
         return False

      else:
         stroke1 = ""
         for symbol in check[:check.index('e')]:
            stroke1 += symbol

         stroke2 = ""
         for symbol in check[check.index('e') + 1:]:
            stroke2 += symbol

         return is_iterable(stroke1) & \
                is_iterable(stroke2)

   # Проверка в случае плавающей запятой
   if '.' in check:
      if check.count('.') != 1 or check[0] == '.' or check[-1] == '.':
         return False

      else:
         stroke1 = ""
         for symbol in check[:check.index('.')]:
            stroke1 += symbol

         stroke2 = ""
         for symbol in check[check.index('.') + 1:]:
            stroke2 += symbol

         return is_iterable(stroke1) & \
                is_iterable(stroke2)

   # Проверка для отрицательных чисел
   else:
      if '-' in check:
         if check.count("-") != 1 or check[0] != "-":
            return False

         else:
            return True

      else:
         return True

# Проверка на целое число. При вводе N1 и N2
def is_int(iterable):

   # Переводим в строку для проверки
   check = str(iterable)
   count_sym = 0

   # Подсчитыаем число символов, возможных при вводе числа
   for num_strings in "0123456789e-":
      count_sym += check.count(num_strings)

   if count_sym != len(check):
      return False

   if '-' in check:

      if check.count("-") != 1 or check[0] != "-":
         return False

      else:
         return True

   else:
      return True

   if 'e' in check:

      if is_int(check) == True:
         check = float(check)

         if int(str(check)[str(check).index(".") + 1:]) == 0:
            return True

         else:
            return False

      else:
         return False

   else:
      return True

# Подсчёт интеграла по методу серединных прямоугольников
def integral_mid(a, b, n):
   integral_sum = 0
   h = (b - a) / n
   current_x = a
   while current_x <= b:
      integral_sum += (f(current_x) + h / 2)

      current_x += h

   return integral_sum * h

# Подсчёт интеграла по методу трапеции
def integral_tranzepoid(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    s *= h / 2
    return s

# Функция для построения таблицы интегралов
def integral_table(leng,leng_ots, aplh_1, aplh_2):
    print("-" * (leng * 3 + 4))
    stroke = "|" + " " * leng \
             + "|" + " " * leng_ots + "N1" + " " * (leng - leng_ots - 2) \
             + "|" + " " * leng_ots + "N2" + " " * (leng - leng_ots - 2) + "|"
    print(stroke)

    # Обработка значений ячеек
    str_method_N1 = f"{aplh_1['N1']:.7g}"
    str_method_N2 = f"{aplh_1['N2']:.7g}"

    print("-" * (leng * 3 + 4))
    stroke = "|" + " " * 4 + "Метод серед треуг." + " " * (leng - 4 - 18) \
             + "|" + " " * leng_ots + str_method_N1 + " " * (leng - leng_ots - len(str_method_N1)) \
             + "|" + " " * leng_ots + str_method_N2 + " " * (leng - leng_ots - len(str_method_N2)) + "|"
    print(stroke)

    # Обработка значений ячеек
    str_method_N1 = f"{aplh_2['N1']:.7g}"
    str_method_N2 = f"{aplh_2['N2']:.7g}"

    print("-" * (leng * 3 + 4))
    stroke = "|" + " " * 6 + "Метод трап." + " " * (leng - 8 - 9) \
             + "|" + " " * leng_ots + str_method_N1 + " " * (leng - leng_ots - len(str_method_N1)) \
             + "|" + " " * leng_ots + str_method_N2 + " " * (leng - leng_ots - len(str_method_N2)) + "|"
    print(stroke)

    print("-" * (leng * 3 + 4))

# Функция для построения таблиц погрешностей
def eps_table(leng, leng_ots, i, aplh_1, aplh_2):
    print("-" * (leng * 3  + 4))
    stroke = "|" + " " * leng \
        + "|" + " " * leng_ots + "N1" + " " * (leng - leng_ots - 2) \
        + "|" + " " * leng_ots + "N2" + " " * (leng - leng_ots - 2) + "|"
    print(stroke)

    # Обработка значений ячеек
    str_method_N1 = f"{aplh_1['N1'][i]:.7g}"
    str_method_N2 = f"{aplh_1['N2'][i]:.7g}"

    print("-" * (leng * 3  + 4))
    stroke = "|" + " " * 4 + "Метод серед треуг." + " " * (leng - 4 - 18) \
        + "|" + " " * leng_ots + str_method_N1 + " " * (leng - leng_ots - len(str_method_N1)) \
        + "|" + " " * leng_ots + str_method_N2 + " " * (leng - leng_ots - len(str_method_N2)) + "|"
    print(stroke)

    # Обработка значений ячеек
    str_method_N1 = f"{aplh_2['N1'][i]:.7g}"
    str_method_N2 = f"{aplh_2['N2'][i]:.7g}"

    print("-" * (leng * 3  + 4))
    stroke = "|" + " " * 6 + "Метод трап." + " " * (leng - 8 - 9) \
        + "|" + " " * leng_ots + str_method_N1 + " " * (leng - leng_ots - len(str_method_N1)) \
        + "|" + " " * leng_ots + str_method_N2 + " " * (leng - leng_ots - len(str_method_N2)) + "|"
    print(stroke)

    print("-" * (leng * 3  + 4))

# Функция для нахождения необходимого количества разбиений при польз.погрешности
def find_intervals(start, end, func, needed_eps):
   if func == "Метод Трапеций":
      n = 1
      while True:
         result_formula = abs(integral_tranzepoid(start, end, n) - integral_tranzepoid(start, end, 2 * n))
         if result_formula < needed_eps:
            return n

         n += 1

   elif func == "Метод Серединных Прямоугольников":
      n = 1
      while True:
         result_formula = abs(integral_mid(start, end, n) - integral_mid(start, end, 2 * n))
         if result_formula < needed_eps:
            return n

         n += 1


# Ввод координат разбиения
is_Correct = False
while is_Correct is False:
   start_ig = input("Введите координату начала разбиения: ")
   end_ig = input("Введите координату конца разбиения: ")
   if (is_iterable(start_ig) & is_iterable(end_ig)) is True:
      start_ig = float(start_ig)
      end_ig = float(end_ig)

      if (start_ig >= end_ig):
         print("Конечная координата интегрирования не может быть меньше или равна начальной")

      else:
         is_Correct = True

   else:
      print("Числа введены некорректно")

# Ввод N1
is_Correct =  False
while is_Correct is False:
   N1 = input("Введите кол-во участков разбиения N1: ")
   if is_int(N1) is True:
      N1 = int(float(N1))
      if N1 <= 0:
         print("Кол-во участков разбиения больше нуля и является целым числом: ")

      else:
         is_Correct = True

   else:
      print("Число введено некорректно")

# Ввод N2
is_Correct =  False
while is_Correct is False:
   N2 = input("Введите кол-во участков разбиения N2: ")
   if is_int(N2) is True:
      N2 = int(float(N2))
      if N2 <= 0:
         print("Кол-во участков разбиения больше нуля и является целым числом: ")

      else:
         is_Correct = True

   else:
      print("Число введено некорректно")

# Подсчёт значения первообразной
real_it = F(end_ig) - F(start_ig)

# Подсчёт методом серединных прямоугольников
# Создаём словарь для упрощения постороения таблицы
mid_method = {'N1': integral_mid(start_ig, end_ig, N1), \
            'N2': integral_mid(start_ig, end_ig, N2)}

# Подсчёт методом трапеций
# Создаём словарь для упрощения постороения таблицы
tranzepoid_method = {'N1': integral_tranzepoid(start_ig, end_ig, N1), \
            'N2': integral_tranzepoid(start_ig, end_ig, N2)}

# Создание словаря с погрешностями
absol_now_N1 = absolute_eps(mid_method['N1'], real_it)
absol_now_N2 = absolute_eps(mid_method['N2'], real_it)
eps_mid = {'N1': [absol_now_N1, relative_eps(absol_now_N1, real_it)], \
            'N2': [absol_now_N2, relative_eps(absol_now_N2, real_it)]}

absol_now_N1 = absolute_eps(tranzepoid_method['N1'], real_it)
absol_now_N2 = absolute_eps(tranzepoid_method['N2'], real_it)
eps_tranzepoid = {'N1': [absol_now_N1, relative_eps(absol_now_N1, real_it)], \
            'N2': [absol_now_N2, relative_eps(absol_now_N2, real_it)]}

# ПОСТРОЕНИЕ ТАБЛИЦ
leng_ots = 10
leng = 24

# Создание таблицы со значениями интегралов
print("Таблица с подсчётами интегралов")
integral_table(leng,leng_ots,mid_method,tranzepoid_method)

# Таблица со значениями абсолютных погрешностей
print("Таблица со значениями абсолютных погрешностей")
eps_table(leng,leng_ots, 0, eps_mid, eps_tranzepoid)

# Таблица со значениями относительных погрешностей
print("Таблица со значениями относительных погрешностей")
eps_table(leng,leng_ots, 1, eps_mid,eps_tranzepoid)

# Ввод пользовательской погрешности
is_Correct = False
while is_Correct is False:
    user_relative_eps = input("Введите относительную погрешность, необходимую для вычисления: ")
    if is_iterable(user_relative_eps) is True:
        user_relative_eps = float(user_relative_eps)
        if user_relative_eps <= 0 or user_relative_eps >= 100:
            print("Относительная погрешность принадлежит (0:100). Введите другое значение")

        else:
            is_Correct = True

    else:
        print("Число введено некорректно")

# Выбираем самую маленькую погрешность, для определения самой эффективной функции
less_eps = min(eps_mid["N1"][1], eps_mid["N2"][1], eps_tranzepoid["N1"][1], eps_tranzepoid["N2"][1])
less_effective_method = ''
# Поиск наименее эффективного метода
if less_eps == eps_mid["N1"][1] or less_eps == eps_mid["N2"][1]:
    less_effective_method = "Метод Трапеций"
else:
    less_effective_method = "Метод Серединных Прямоугольников"

# Вывод менее эффективного метода
print("Менее эффективный метод: " + less_effective_method)
# Вывод необходимого количества участков
N = find_intervals(start_ig, end_ig, less_effective_method, user_relative_eps)
print("Для достижения данной точности потребуется кол-во участков, равное: " + str(N))