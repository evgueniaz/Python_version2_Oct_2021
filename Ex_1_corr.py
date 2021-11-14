<<<<<<< Updated upstream
# Выяснить тип результата выражений:
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
=======


def num_translate(num):
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    try:
        return print(numbers[num])
    except:
        return print('None')

num_translate('five')
>>>>>>> Stashed changes
