

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]

# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А'
# ]

klasses = ['9А', '7В']

klasses += [None] * (len(tutors) - len(klasses))
tuples = ((tutor, klass) for tutor, klass in zip(tutors,klasses))

print(type(tuples))
print(*tuples)


# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))
# print(next(tuples))

# print(next(tuples), next(tuples), next(tuples), sep=', ')
# print(next(tuples), next(tuples), next(tuples), sep=', ')
# print(next(tuples), next(tuples), next(tuples), sep=', ')
