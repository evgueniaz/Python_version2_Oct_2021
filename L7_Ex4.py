# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя
# граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

size_list = []
my_dir = r'C:\Users\evgue\Documents\Документы'
for el in os.listdir(my_dir):
    path = os.path.join(my_dir, el)
    if os.path.isfile(path):
        print(el, os.stat(path).st_size)


for root, dirs, files in os.walk(my_dir):
    for dir in dirs:
        path = os.path.join(root, dir)
        for el in os.listdir(path):
            in_path = os.path.join(path, el)
            if os.path.isfile(in_path):
                el_size = os.stat(in_path).st_size
                print(el, el_size)
                size_list.append(el_size)
size_list.sort()

print(size_list)

files_by_size = {}
for el in size_list:
    upper_limit = (el // 100 + 1) * 100
    if upper_limit in files_by_size:
        files_by_size[upper_limit] += 1
    else:
        files_by_size[upper_limit] = 1
print(files_by_size)



