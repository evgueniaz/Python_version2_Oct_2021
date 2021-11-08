
rooster = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i in range(len(rooster)):
    if rooster[i].isnumeric():
        rooster[i] = (rooster[i]).zfill(2)
        rooster.insert(i, '"')
        rooster.insert(i + 2, '"')
        i += 3
    elif '+' in rooster[i] or '-' in rooster[i]:
        rooster[i] = (rooster[i]).zfill(3)
        rooster.insert(i, '"')
        rooster.insert(i + 2, '"')
        i += 3

    else:
        i += 1

phrase = ' '.join(rooster)
print(rooster)
print(phrase)