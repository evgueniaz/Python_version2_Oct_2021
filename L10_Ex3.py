
class Cell():
    nucleus: int

    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        sum = self.nucleus + other.nucleus
        return f"A new cell with {sum} nuclei"

    def __sub__(self, other):
        difference = self.nucleus - other.nucleus
        if difference > 0:
            return f"A new cell with {difference} nuclei"
        else:
            return f'An impossible action'

    def __mul__(self, other):
        product = self.nucleus * other.nucleus
        return f"A new cell with {product} nuclei"

    def __floordiv__(self, other):
        quotient = self.nucleus // other.nucleus
        return f"A new cell with {quotient} nuclei"

    def __truediv__(self, other):
        quotient = round(self.nucleus / other.nucleus)
        return f"A new cell with {quotient} nuclei"

    def makeorder(self, row):
        row_number = self.nucleus // row
        last_row = self.nucleus % row
        symbol = "*"
        if last_row == 0:
            result = '\n'.join([''.join(symbol * row) for i in range(row_number)])
        else:
            result = '\n'.join([''.join(symbol * row) for i in range(row_number - 1)]) + '\n' + ''.join(symbol * last_row)
        return f"Order of nuclei is \n{result}"

    def __str__(self):
        return f"A cell with {self.nucleus} nuclei"


n = Cell(23)
print(n)

m = Cell(41)
k = Cell(15)
print(n + m)
print(n - m)
print(m - n)
print(n * m)
print(m // k)
print(m / k)
print(n.makeorder(4))
print(m.makeorder(6))
print(k.makeorder(5))

