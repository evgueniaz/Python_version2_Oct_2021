
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import randrange, choice

jokes = []
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """Счетчик шуток"""
    i = 0
    while i < n:
        """Склеивает случайно выбранные слова из каждого списка и добавляет в список jokes"""
        jokes.append(choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives))
        i += 1
    return print(jokes)

get_jokes(2)

