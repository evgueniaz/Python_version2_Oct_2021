

from pprint import pprint
lists = {}

def thesaurus_adv(*names):

    for el in names:
        if el.split()[1][0] not in lists:
            lists[el.split()[1][0]] = [el]

        else:
            lists[el.split()[1][0]].append(el)

    for el in lists:
        name_lists = {}
        for i in lists[el]:
            if i[0] in name_lists:
                name_lists[i[0]].append(i)
            else:
                name_lists[i[0]] = [i]
        lists[el] = name_lists

    return pprint(lists)

thesaurus_adv("Иван Сергеев", "Светлана Ляпкина", "Инна Серова","Инесса Ильина", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Алексей Андреев", "Надежда Ивашкина", "Роман Андронов", "Федор Левашов")

# sorted_lists = dict(sorted(lists.items(), key=lambda x: x[1]))
# print(sorted_lists)


