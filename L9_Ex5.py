
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Рисунок ручкой')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисунок карандашом')

class Handle(Stationery):
    def draw(self):
        print(f'Рисунок маркером')

x = Pencil('Rembrandt')
x.draw()

y = Pen('Duerer')
y.draw()

z = Handle('Bunker')
z.draw()

t = Stationery('Miller')
t.draw()
