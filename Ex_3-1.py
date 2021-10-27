
data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in data:
    person = el.split()
    person[-1] = (person[-1]).capitalize()
    print(f'Привет, {person[-1]} !')


