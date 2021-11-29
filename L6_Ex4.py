
import json

lines = {}
name_data = ['Фамилия', 'Имя', 'Отчество']

f = open('users.txt', 'r', encoding='utf-8')
h = open('hobby.txt', 'r', encoding='utf-8')
for line in f:
    names = line.split()[0]
    names = names.split(',')
    hobbies = h.readline().rstrip('\n')
    hobbies = hobbies.split(',')
    if hobbies == ['']:
        hobbies = None
    person = dict(zip(name_data, names))
    person_data = ' '.join(names)
    print(person)
    lines[person_data] = hobbies

hobbies = h.readline()
if hobbies != '':
    raise SystemExit(1)
else:
    print(lines)
h.close()
f.close()

with open('hobby_list_new.json', 'w', encoding='utf-8') as hln:
    json.dump(lines, hln, ensure_ascii=False, indent=4)