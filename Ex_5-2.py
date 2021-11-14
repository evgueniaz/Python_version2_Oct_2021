
from random import randrange, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num=1, repetion_allowance=True):
    jokes = []
    """Счетчик шуток"""
    i = 0
    if repetion_allowance is True:
        while i < num:
            """Склеивает случайно выбранные слова из каждого списка и добавляет в список jokes. 
            Возможны повторения"""

            jokes.append(choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives))
            i += 1
    else:
        while i < num:
            """Склеивает случайно выбранные слова из каждого списка и добавляет в список jokes.
              Без повторений"""

            jokes.append(nouns.pop(randrange(len(nouns))) + ' ' + adverbs.pop(randrange(len(adverbs))) + ' '
                         + adjectives.pop(randrange(len(adjectives))))
            i += 1
    return print(jokes)


# get_jokes(5)
# get_jokes(5, False)
get_jokes(3)
get_jokes(4, False)

