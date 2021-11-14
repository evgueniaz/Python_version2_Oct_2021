
rooster = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i in range(len(rooster)):
    if rooster[i].isnumeric():
        rooster[i] = (rooster[i]).zfill(2)
        rooster.insert(i, '"')
        rooster.insert(i + 2, '"')
        i += 3
    elif '+' in rooster[i] or '-' in rooster[i]:
        rooster[i] = (rooster[i]).zfill(3)
        rooster.insert(i, '"')
        rooster.insert(i + 2, '"')
        i += 3

<<<<<<< Updated upstream
=======

def num_translate_adv(num):
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if num.istitle() is False:
        try:
            return print(numbers[num])
        except:
            return print('None')
>>>>>>> Stashed changes
    else:
        i += 1

phrase = ' '.join(rooster)
print(rooster)
print(phrase)
