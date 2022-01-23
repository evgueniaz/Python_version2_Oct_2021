# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def transform(cls, date):
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:8])
        print(f'day - {day}, month - {month}, year - {year}')

    @staticmethod
    def proof(date):
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:8])
        if day < 1 or day > 31:
            return f'An invalid day'
        if month < 1 or month > 12:
            return f'An invalid month'
        if month ==2 and day > 29:
            return f'An invalid day'
        if year < 1:
            return f'An invalid year'
        else:
            return "It's a valid date"

Date.transform('12-03-2009')
# print(Date('12-3-2009'))
print(Date.proof('12-03-2009'))
print(Date.proof('30-02-2016'))
