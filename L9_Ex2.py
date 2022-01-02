class Road:
    _length = float
    _width = float

    def __init__(self, _length, _width, density=25, thickness=5):
        self._length = _length
        self._width = _width
        self.density = density
        self.thickness = thickness

    def mass(self):
        # длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
        # 1 см*число см толщины полотна
        total_mass = self._length * self._width * self.density * self.thickness
        if total_mass > 1000:
            print(f'Масса асфальта для покрытия всего дорожного полотна составляет  {total_mass / 1000}  т')
        else:
            print(f'Масса асфальта для покрытия всего дорожного полотна составляет  {total_mass}  кг')


road_1 = Road(5, 10)
road_2 = Road(120, 15)
road_3 = Road(5000, 20)

# 20 м *5000 м * 25 кг/(м2*см) * 5 см = 12500 т

road_1.mass()
road_2.mass()
road_3.mass()

