# Пресняков А.К. ИУ7-13Б. Лабораторная работа 12

from string import *

# Создаём алфавиты со всеми необходимыми символами
english_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
russian_letters = 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
numbers = '0123456789'
punct = " —.,!?..-:()\""




# Основное меню
def menu(text):
    text_output(text)
    print()
    print("Список команд:")
    print("1. Выравнять текст по левому краю")
    print("2. Выравнять текст по правому краю")
    print("3. Выравнять текст по ширине")
    print("4. Удаление всех вхождений заданного слова")
    print("5. Замена одного слова другим во всём тексте")
    print("6. Вычсилить арифметические выражения из текста, умножение и деление")
    print("7. Найти самое длинное по количеству слов предложение и удалить")
    print()
    print("0. Выход")
    print()
    user_charge = charge_input()
    print()
    return user_charge

# Разветвитель команд
def charge_starter(charge,text):
    if charge == 1:
        leftside_lining(text)
    elif charge == 2:
        rightside_lining(text)
    elif charge == 3:
        wide_lining(text)
    elif charge == 4:
        all_ins_delete(text)
    elif charge == 5:
        change_word(text)
    elif charge == 6:
        perform_arethmitical_expressions(text)
    elif charge == 7:
        most_words_sentnce(text)

# Исходный текст в форме функции (необходимо для того, чтобы текст возвращался в исходное состояние)
def main_text():
    text = [' Осень - самое печальное время года. Деревья остаются совсем ',
            ' пустыми, уже нет их 5*2//3+3 одеяний. А листься, когда-то',
            ' весело покачивающиеся на ветру медленно погибают. Вот так,',
            ' осенью идут дожди, осенью 12//4 небо чёрное как тьма. То ли от таких',
            ' приколов, что те одинокие деревья стоят на ветру 24*7 часов сутки.']
    return text

# Вывод текста
def text_output(text_lines):
    for line in text_lines:
        print(line)
    return

# Ввод команды пользователем
def charge_input():
    charge = None
    while charge is None:
        try:
            charge = int(input("Введите номер команды: "))
        except ValueError:
            print("Вы ввели не число! Повторите ввод.")
            charge = None
        else:
            if charge < 0 or charge > 7:
                print("Команды под таким номером не существует! Повторите ввод.")
                charge = None
    return charge

def user_word_input():
    is_Correct = False
    while not(is_Correct):
        s = input(str("Введите слово: "))
        if s.count(" ") == len(s):
            print("Вы ввели пустую строчку!")
            is_Correct = False
        else:
            is_Correct = True
        for i in digits:
            if i not in s:
                is_Correct = True
            else:
                is_Correct = False
                print("Слово не может содержать цифры!")
                break
    return s



# РЕДАКТИРОВАНИЕ ТЕКСТА

# Устранение пробелов в правой части текста
def right_spaces_clear(text):
    for j in range(len(text)):
        while len(text[j]) > 1 and text[j][-1] == " ":
            text[j] = text[j][:len(text[j]) - 1]

# Выравнивание по левой стороне
def leftside_lining(text):
    if len(text) == 0:
        print("Текст пуст")
        return
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ", 1)

    for j in range(len(text)):
        index = 0
        while text[j][index] == " ":
            index += 1
        text[j] = text[j][index:]


# Выравнивание по правой стороне
def rightside_lining(text):
    if len(text) == 0:
        print("Текст пуст")
        return
    right_spaces_clear(text)
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ", 1)

    max_len = len(max(text, key=lambda x: len(x)))
    for j in range(len(text)):
        text[j] = " " * (max_len - len(text[j])) + text[j]

# Выравнивание по ширине
def wide_lining(text):
    if len(text) == 0:
        print("Текст пуст")
        return
    leftside_lining(text)
    right_spaces_clear(text)
    max_len = len(max(text, key=lambda x: len(x)))
    for num in range(len(text)):
        spaces = (max_len - len(text[num]))

        while spaces > 0:
            index = 0

            while index < len(text[num]):

                if text[num][index] == " ":

                    while text[num][index] == " ":
                        index += 1

                    text[num] = text[num][:index] + " " + text[num][index:]
                    spaces -= 1
                index += 1

                if spaces == 0:
                    break

# Удаление слова
def all_ins_delete(text):
    if len(text) == 0:
        print("Текст пуст")
        return
    word = user_word_input()
    word = word.lower()
    print()
    for sent_index in range(len(text)):
        change_sent = ' ' + text[sent_index] + ' '
        border = 1
        while border < len(change_sent) - 1 - len(word):

            if (change_sent[border:border + len(word)]).lower() == word and \
                    ((change_sent[border - 1] in punct) and
                     (change_sent[border + len(word)] in punct)):

                change_sent = change_sent[0:border] + change_sent[border + len(word):]
                border += (1 - len(word))

            else:
                border += 1

        if change_sent[0] == ' ':
            change_sent = change_sent[1:]

        text[sent_index] = change_sent

# Замена слова
def change_word(text):
    if len(text) == 0:
        print("Текст пуст")
        return
    print("Введите слово, на которое хотите заменить")
    change = user_word_input()
    print("Введите заменямое слово")
    replacable = user_word_input()
    replacable = replacable.lower()
    for sent_index in range(len(text)):
        change_sent = ' ' + text[sent_index] + ' '
        border = 1
        while border < len(change_sent) - 1 - len(replacable):

            if (change_sent[border:border + len(replacable)]).lower() == replacable and \
                ((change_sent[border - 1] in punct) and
                (change_sent[border + len(replacable)] in punct)):

                change_sent = change_sent[0:border] + change + change_sent[border + len(replacable):]
                border += (len(change) - len(replacable) + 1)

            else:
                border += 1

        if change_sent[0] == ' ':
            change_sent = change_sent[1:]

        text[sent_index] = change_sent

# Вычисление арифметического выражения
# Проверка подсчёта
def try_to_count(num1, num2, operation, stroke):
    if len(num1) == (num1.count('-') + num1.count('+')) or len(num2) == (num2.count('-') + num2.count('+')):
        return False

    if operation == "*":
        if len(num1) + len(num2) + stroke.count(" ") + 1 == len(stroke):
            return True

        else:
            return False
    if operation == "//":
        if len(num1) + len(num2) + stroke.count(" ") + 2 == len(stroke):
            return True

        else:
            return False


# Поиск и подсчёт
def detect_and_count(stroke, start):
    if len(text) == 0:
        print("Текст пуст")
        return
    stroke += ' '
    index_nums = []
    index = start
    while index < len(stroke):
        if stroke[index] in numbers:
            start_ID = index
            len_num = 1
            index += 1

            while index < len(stroke) and stroke[index] in numbers:
                len_num += 1
                index += 1

            index_nums.append([start_ID, len_num])

        elif stroke[index] in '+-':
            start_ID = index
            len_num = 1
            index += 1

            while index < len(stroke) and stroke[index] in numbers and stroke[start_ID + 1] in numbers:
                len_num += 1
                index += 1

            index_nums.append([start_ID, len_num])

        index += 1

    if len(index_nums) <= 1:
        return [stroke, False, 0]

    else:
        for i in range(len(index_nums) - 1):
            check_stroke = stroke[index_nums[i][0]:(index_nums[i + 1][0] + index_nums[i + 1][1])]
            cnum1 = stroke[index_nums[i][0]:(index_nums[i][0] + index_nums[i][1])]
            cnum2 = stroke[index_nums[i + 1][0]:(index_nums[i + 1][0] + index_nums[i + 1][1])]

            if ('*' in check_stroke and check_stroke.count('*') == 1 and '/' not in check_stroke):

                if try_to_count(cnum1, cnum2, "*", check_stroke) is True:
                    converted = str(int(cnum1) * int(cnum2))

                    stroke = stroke[:index_nums[i][0]] + converted + stroke[
                                                                     (index_nums[i + 1][0] + index_nums[i + 1][1]):]

                    return [stroke, True, 0]

            elif ('*' not in check_stroke and '//' in check_stroke and check_stroke.count('/') == 2):

                if try_to_count(cnum1, cnum2, "//", check_stroke) is True:
                    try:
                        converted = str(int(cnum1) // int(cnum2))
                        stroke = stroke[:index_nums[i][0]] + converted + stroke[
                                                                         (index_nums[i + 1][0] + index_nums[i + 1][1]):]

                        return [stroke, True, 0]

                    except Exception:

                        return [stroke, True, index_nums[i + 1][0]]

        return [stroke, False, 0]

# Замена на подсчитанное
def perform_arethmitical_expressions(text):
    for stroke in range(len(text)):
        work_indicator = True
        start_id = 0

        while work_indicator is True:
            result_if = detect_and_count(text[stroke], start_id)

            text[stroke] = result_if[0]
            work_indicator = result_if[1]
            start_id = result_if[2]

            continue

# Удаление самого большого по количеству слов предложения
def most_words_sentnce(text):
    count_words = []
    words_count = 0
    if len(text) == 0:
        print("Текст пуст")
        return
    if len(text) == 1:
        text.pop(0)
        return
    for i in range(len(text)):
        stroke = text[i]
        border = 0
        while border < len(stroke):
            if stroke[border] in '?!.':
                count_words.append(words_count)
                words_count = 0
                border += 1

            elif stroke[border] not in punct:
                while border < len(stroke) and stroke[border] not in punct:
                    border += 1
                words_count += 1

            else:
                border += 1
    words_count = 0
    sym_count = 0
    for i in range(len(text)):
        stroke = text[i]
        border = 0
        while border < len(stroke):
            if stroke[border] in '?!.':
                if words_count == max(count_words):
                    stroke_print = text[i][:border+1]
                    text[i] = text[i][border+1:]
                    if i == 0:
                        print(stroke_print)
                        return
                    if len(text[i]) == 0:
                        text.pop(i)
                    if '.' not in text[i-1]:
                        stroke_print = text[i - 1] + stroke_print
                        text.pop(i - 1)
                        break
                    if i != 0:
                        if "." in text[i-1]:
                            stroke_print = text[i-1][text[i-1].index(".") + 1:] + stroke_print
                            text[i-1] = text[i-1][:text[i-1].index(".") + 1]
                            print(stroke_print)
                            print()
                            break
                        elif "?" in text[i-1]:
                            stroke_print = text[i - 1][text[i - 1].index("?") + 1:] + stroke_print
                            text[i-1] = text[i-1][:text[i-1].index("?") + 1]
                            print(stroke_print)
                            print()
                            break
                        elif "!" in text[i-1]:
                            stroke_print = text[i - 1][text[i - 1].index("!") + 1:] + stroke_print
                            text[i-1] = text[i-1][:text[i-1].index("!") + 1]
                            print(stroke_print)
                            break

                words_count = 0
                border += 1

            elif stroke[border] not in punct:
                while border < len(stroke) and stroke[border] not in punct:
                    border += 1
                words_count += 1

            else:
                border += 1


# Вызов программы
text = main_text()
while True:
    charge_main = menu(text)
    if charge_main == 0:
        break
    else:
        charge_starter(charge_main, text)
# вот такие пирог. вт тк прг. ВОТ ТАКИИИЕ ПИИРОГИИИ.