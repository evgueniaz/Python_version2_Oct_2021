#show_sale.py

import sys

with open(r'C:\Users\evgue\PycharmProjects\Geek_Python_2\Lesson_6\bakery.txt', 'r+', encoding='utf-8') as f:

    if len(sys.argv) > 3:
        print('Вы передали в сценарий слишком много аргументов')
        sys.exit()

    if len(sys.argv) == 1:
        sales = f.read()
        print(sales)

    if len(sys.argv) == 2:
        start_list = int(sys.argv[1]) - 1
        for idx, line in enumerate(f):
            if idx >= start_list:
                print(line.rstrip('\n'))

    if len(sys.argv) == 3:
        start_list = int(sys.argv[1]) - 1
        end_list = int(sys.argv[2]) - 1
        for idx, line in enumerate(f):
            if idx >= start_list and idx <= end_list:
                print(line.rstrip('\n'))
