# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, warehouse_name, address):
        self.warehouse_name = warehouse_name
        self.address = address
        self._list = {}

    def add_to(self, devices):
        self._list.setdefault(devices.group_name(), []).append(devices)

    def extract(self, name):
        if self._list[name]:
            self._list.setdefault(name).pop(0)

    def __str__(self):
        return f"Warehouse {self.warehouse_name}, located at {self.address}"

class Devices(Warehouse):

    def __init__(self, name, amount, year):
        self.name = name
        self.amount = amount
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} - amount available is {self.amount}, production year {self.year}'


class Printer(Devices):

    def __init__(self, speed, saturation, cartridge_resource, name, amount, year):
        super().__init__(name, amount, year)
        self.speed = speed
        self.saturation = saturation
        self.cartridge_resource = cartridge_resource

    def __repr__(self):
        return f"{self.name}, made in {self.year} - {self.amount} printers are available. \nPrinting speed is {self.speed} " \
               f"pages per min. \nSaturation is {self.saturation} %. \nCartridge resource is {self.cartridge_resource} pages."

    def action(self):
        return 'Prints'


class Scanner(Devices):

    def __init__(self, speed, quality, name, amount, year):
        super().__init__(name, amount, year)
        self.quality = quality
        self.speed = speed

    def __repr__(self):
        return f"{self.name}, made in {self.year} - {self.amount} scanners are available. " \
               f"\nScanning speed is {self.speed} pages per min.  \nScanning quality {self.quality}"

    def action(self):
        return 'Scans'

class Copier(Devices):

    def __init__(self, sites_per_page, name, amount, year):
        super().__init__(name, amount, year)
        self.sites_per_page = sites_per_page

    def __repr__(self):
        return f"{self.name}, made in {self.year} - {self.amount} copiers are available. " \
               f"\nCopying speed is {self.speed} pages per min.  \nCopies {self.sites_per_page} sites per page."

    def action(self):
        return 'Makes a copy'

w = Warehouse('Skald_1', 'Sofiyskaya_60')
print(w)
# p = Printer(15, 80, 3000, 'Epson_1', 3, 2018)
# print(p)

# w = Warehouse
scanner = Scanner(5, 'draft', 'hp_1', 2, 2004)
print(scanner.action)
w.add_to(scanner)
scanner = Scanner(4, 'photo', 'Epson_2', 1, 2010)
w.add_to(scanner)
scanner = Scanner(6, 'standard', 'Brothers_1', 3, 2019)
w.add_to(scanner)
printer = Printer(20, 70, 5000, 'Epson_1', 2, 2016)
w.add_to(printer)
printer = Printer(15, 80, 3000, 'Epson_2', 3, 2018)
w.add_to(printer)

print(w._list)

# w.extract(scanner)
# print()
# print(w._list)