
def odd_nums(n):
    nums_gen = (nums for nums in range(1, n + 1, 2))
    return nums_gen

print(type(odd_nums(15)))
print(*odd_nums(15))



