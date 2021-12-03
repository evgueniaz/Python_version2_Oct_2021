
import json

with open('users.txt', 'r', encoding='utf-8') as f:
    names = f.read().splitlines()
    # print(names)

with open('hobby.txt', 'r', encoding='utf-8') as h:
    hobbies = h.read().splitlines()
    # print(hobbies)

if len(names) >= len(hobbies):
    hobbies += [None] * (len(names) - len(hobbies))
    lines = dict(zip(names, hobbies))
    print(lines)
else:
    raise SystemExit(1)


with open('hobby_list.json', 'w', encoding='utf-8') as hl:
    json.dump(lines, hl, ensure_ascii=False, indent=4)

