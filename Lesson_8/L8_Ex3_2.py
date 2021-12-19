# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы
# вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли
# вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)



def type_logger(func):
    result = {}
    full_result = []
    def wrapper(*args):
        nonlocal result, full_result
        for num in args:
            argument = num
            argument_type = type(num)
            value = func(num)
            value_type = type(value)
            result = {'argument': argument, 'argument_type': argument_type, 'value': value, 'value_type': value_type}
            full_result.append(result)
        # return full_result
        return f'{func.__name__} {full_result}'
    return wrapper

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5, 2, 4.1, -8.2)
print(a)