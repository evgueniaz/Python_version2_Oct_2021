# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список
# необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.

class NumericalValueError(Exception):
    def __init__(self, txt):
        self.txt = txt

rooster = []

while True:
    item = input("Enter a numerical value to be added to your list: \n(To stop entering numbers press ENTER) >>>  ")
    if item == "":
        print(f"Your rooster is: {rooster}")
        break

    try:
        if item.isnumeric() is False:
            raise NumericalValueError("You've entered a non-numerical value!")
    except ValueError:
        print("You've entered a non-numerical value!")
    except NumericalValueError as err:
        print(err)
    else:
        rooster.append(item)


