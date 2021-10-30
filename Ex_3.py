
declination = ['процент', 'процента', 'процентов']

i = 1
while i < 101:
    if i % 10 == 1 and i != 11:
        print(f'{i}  {declination[0]}')
    elif i % 10 == 2 and i != 12 or i % 10 == 3 and i != 13 or i % 10 == 4 and i != 14:
        print(f'{i}  {declination[1]}')
    else:
        print(f'{i}  {declination[2]}')
    i += 1