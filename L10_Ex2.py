
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cloth(self, coat_number, jacket_number):
        pass

    def cloth_size(self, coat_number, jacket_number, size, height):
        return f"Cloth needed for {coat_number} coats and {jacket_number} jackets is  " \
               f"{(size / 6.5 + 0.5) * coat_number + (2 * height + 0.3) * jacket_number}"


class Coat(Clothes):
    def __init__(self, size, amount):
        self.v = size
        self.x = amount

    @property
    def size(self):
        return self.v

    def cloth(self, v, x):
        coat_cloth = x * (v / 6.5 + 0.5)
        return f'Cloth needed for {x} coats is {coat_cloth}'

class Jacket(Clothes):
    def __init__(self, height, amount):
        self.h = height
        self.y = amount

    def cloth(self, h, y):
        jacket_cloth = y * (2 * h + 0.3)
        return f'Cloth needed for {y} jackets is {jacket_cloth}'


c = Coat(52, 3)
j = Jacket(185, 2)

print(c.cloth(52, 3))
print(j.cloth(185, 2))
print(c.cloth_size(3, 2, 52, 185))

