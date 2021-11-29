
#add_sale.py


import sys

with open(r'C:\Users\evgue\PycharmProjects\Geek_Python_2\Lesson_6\bakery.txt', 'a+', encoding='utf-8') as f:
    if len(sys.argv) > 2:
        print('You entered too many arguments')
        sys.exit()
    if len(sys.argv) < 1:
        print('You must enter one sales result')
        sys.exit()

    add_sale = sys.argv[1]
    f.write(add_sale + '\n')


