duration = int(input("Введите время в секундах ---"))

d = duration // 86400
remainder_hours = duration % 86400
h = remainder_hours // 3600
remainder_minutes = remainder_hours % 3600
m = remainder_minutes // 60
s = remainder_minutes % 60
print(f"{d}  дн  {h}  час  {m}  мин  {s}  сек")
