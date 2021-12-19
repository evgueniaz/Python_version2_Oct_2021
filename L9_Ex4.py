# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.color} {self.name} поехала')

    def stop(self):
        print(f'Машина {self.color} {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.color} {self.name} {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.color} {self.name}! Скорость превышена')
        else:
            print(f'Машина {self.color} {self.name}! Текущая скорость автомобиля {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.color} {self.name}! Скорость превышена')
        else:
            print(f'Машина {self.color} {self.name}! Текущая скорость автомобиля {self.speed} км/ч')


class PoliceCar(Car):
    def show_speed(self):
        if self.is_police is True:
                if self.speed > 60:
                    print(f'Полиция! Уступите дорогу!')
                else:
                    print(f'Полиция осуществляет патрулирвоание')
        else:
            print(f'Машина {self.color} {self.name} не является полицейской машиной')

town = TownCar(90, 'black', 'Audi', False)
town.show_speed()

work = WorkCar(35, 'white', 'Nissan', True)
work.show_speed()

car_1 = Car(89, 'silver', 'Toyota', False)
car_1.show_speed()
car_1.go()
car_1.turn('налево')
car_1.stop()

car_2 = PoliceCar(78, 'white', 'Chevrolet', is_police=True)
car_2.show_speed()

