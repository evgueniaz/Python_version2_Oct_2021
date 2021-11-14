

lists = {}
def thesaurus(*names):
    for el in names:
        if el[0] in lists:
            lists[el[0]].append(el)
        else:
            lists[el[0]] = [el]
    return print(lists)

thesaurus("Иван", "Мария", "Петр", "Илья", "Алексей", "Матвей", "Анна", "Сергей", "Леонид")

sorted_lists = dict(sorted(lists.items(), key=lambda x: x[1]))
print(sorted_lists)
