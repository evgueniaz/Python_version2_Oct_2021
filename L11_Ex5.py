# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_number:

    def __init__(self, a, b):
        self.real_part = a
        self.imaginary_part = b

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary =self.imaginary_part + other.imaginary_part
        return f'Result of addition is: {real} + {imaginary}i'

    def __mul__(self, other):
        real = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return f'Result of addition is: {real} + {imaginary}i'

x = Complex_number(2, 3)
y = Complex_number(3, -1)
print(x + y)
print(x * y)