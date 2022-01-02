class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position

        self._income = {'salary': salary, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Имя и Фамилия:   {self.name} {self.surname}')

    def get_total_income(self):
        total_income = sum(self._income.values())
        print(f'Совокупный доход составляет  -  {total_income}')

p = Position('Sam', 'Smith', 'manager', 15000, 7500)
p.get_full_name()
p.get_total_income()

