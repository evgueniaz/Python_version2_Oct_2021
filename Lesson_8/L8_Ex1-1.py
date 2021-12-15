# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

import re

def email_parse():

    email_address = input('Введите адрес электронной почты >>>  ')

    if (re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_address)):
        username = re.compile(r'(\S+)(?=@)')
        domain = re.compile(r'(?<=@)(\S+.\w+)')
        # result = re.split(r'[@]', email_address)
        # correo = {'username': username.search(email_address).group(), 'domain': domain.search(email_address).group()}
        # print(username.search(email_address).group())
        # print(domain.search(email_address).group())
        correo = {'username': username.search(email_address).group(), 'domain': domain.search(email_address).group()}
        # print(result)
        print(correo)
    else:
        raise ValueError ('Некорректный адрес электронной почты')

email_parse()