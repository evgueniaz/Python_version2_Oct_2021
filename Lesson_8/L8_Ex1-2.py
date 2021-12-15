import re


def email_parse():
    email_address = input('Введите адрес электронной почты >>>  ')

    if (re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_address)):
        result = re.split(r'[@]', email_address)
        correo = {'username': result[0], 'domain': result[1]}
        print(correo)
    else:
        raise ValueError('Некорректный адрес электронной почты')


email_parse()