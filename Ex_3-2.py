data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i = 0
for el in data:
    item = el.split()[:-1]
    item.append(el.split()[-1].capitalize())
    print(f'Привет, {el.split()[-1].capitalize()} !')
    el = ' '.join(item)
    data[i] = el
    i += 1

print(data)
