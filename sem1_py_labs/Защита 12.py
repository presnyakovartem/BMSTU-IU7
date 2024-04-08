# Исходный текст в форме функции (необходимо для того, чтобы текст возвращался в исходное состояние)
def main_text():
    text = [' Осень - самое печальное время года. Деревья остаются совсем ',
            ' пустыми, уже нет их 5*2//3+3 одеяний. А листься, когда-то',
            ' весело покачивающиеся на ветру медленно погибают. Вот так,',
            ' осенью идут дожди, осенью 12//4 небо чёрное как тьма. То ли от таких',
            ' приколов, что те одинокие деревья стоят на ветру 24*7 часов сутки.']
    return text

russian_voplume = 'еоаяиюыёЭОАЯИЮЫЁ'
russian_unvolume = 'цкнгшщзхфвпрлджчсмтьбъЙЦКНГШЩЗХФВПРЛДЖЧСМТЬБЪ'
punct = " —.,!?..-:()\""

def most_words_gl_sogl_sentence(text):
    count_words = []
    words_count = 0
    for i in range(len(text)):
        stroke = text[i]
        border = 0
        while border < len(stroke):
            if stroke[border] in '?!.':
                count_words.append(words_count)
                words_count = 0
                border += 1

            elif stroke[border] not in punct:
                flag = True
                while border < len(stroke) and stroke[border] not in punct:
                    if (stroke[border] in russian_volume and stroke[border+1] in russian_unvolume)\
                        or (stroke[border+1] in russian_volume and stroke[border-1] in russian_unvolume):
                        continue
                    else:
                        flag = False

                    border += 1
                if flag:
                    words_count += 1

            else:
                border += 1

    return count_words
text1 = main_text()
print(most_words_gl_sogl_sentence(text1))