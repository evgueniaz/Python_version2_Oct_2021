


def num_translate_adv(num):
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if num.istitle() is False:
        try:
            return print(numbers[num])
        except:
            return print('None')
    else:
        cap_num = num.lower()
        try:
            return print(numbers[cap_num].capitalize())
        except:
            return print('None')

num_translate_adv('Five')
num_translate_adv('ten')
num_translate_adv('red')
num_translate_adv('Sad')
num_translate_adv('Eight')
