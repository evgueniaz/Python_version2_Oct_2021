# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

dividend = input("Enter a numerical dividend: ")
divisor = input("Enter a numerical divisor: ")

try:
    dividend = int(dividend)
except ValueError:
    print("You've entered a non-numerical value!")
else:
    try:
        divisor = int(divisor)
        if divisor == 0:
            raise ZeroDivisionError("You try to devide by zero!")
    except ValueError:
        print("You've entered a non-numerical value!")
    except ZeroDivisionError as err:
        print(err)
    else:
        print(f"The result of division of {dividend} / {divisor} is {dividend / divisor}")

