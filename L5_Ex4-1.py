
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

result = []
result.append(y for x, y in zip(src[:-1], src[1:]) if y > x)

print(type(result))
print([*result[0]])




