#corr_sale.py

import sys

with open(r'C:\Users\evgue\PycharmProjects\Geek_Python_2\Lesson_6\bakery.txt', 'r+', encoding='utf-8') as f:

    if len(sys.argv) > 3:
        print('Вы передали в сценарий слишком много аргументов')
        sys.exit()

    sales = []
    corr_idx = int(sys.argv[1])
    corr_sale = sys.argv[2]

    for idx, line in enumerate(f, 1):
        if idx != corr_idx:
            sales.append(line)
        else:
            sales.append(corr_sale + '\n')
    print(sales)

with open(r'C:\Users\evgue\PycharmProjects\Geek_Python_2\Lesson_6\bakery.txt', 'w+', encoding='utf-8') as f:
    f.writelines(sales)
