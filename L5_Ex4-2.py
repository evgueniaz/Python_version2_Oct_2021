
result = []
result = [y for x, y in zip(src[:-1], src[1:]) if y > x]

print(type(result))
print(result)
