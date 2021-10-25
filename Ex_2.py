
rooster = []
i = 0
x = 1
while x <= 1000:
    rooster.append(x ** 3)
    x += 2

numbers_sum, numbers_sum_aug = 0, 0
for el in rooster:
    digit_sum, remainder = 0, 0
    quotient = el
    while quotient > 0:
        remainder = quotient % 10
        quotient = quotient // 10
        digit_sum += remainder
    if digit_sum % 7 == 0:
        numbers_sum += el

for i in range(len(rooster)):
    digit_sum_aug, remainder_aug = 0, 0
    quotient_aug = rooster[i] + 17
    while quotient_aug > 0:
        remainder_aug = quotient_aug % 10
        quotient_aug = quotient_aug // 10
        digit_sum_aug += remainder_aug
    if digit_sum_aug % 7 == 0:
        numbers_sum_aug += rooster[i]


# print(rooster)
print(f'Сумма чисел списка, сумма цифр которых делится без остатка на 7 = {numbers_sum}')
print(f'Сумма чисел нового списка, сумма цифр которых делится без остатка на 7 = {numbers_sum_aug}')