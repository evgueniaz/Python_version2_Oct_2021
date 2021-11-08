# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# •	Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# •	Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# •	Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# •	Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

prices = [57.8, 46.51, 97, 34.21, 102.02, 12.45, 85, 98.56, 42.90, 27, 74.98, 40.67]
new_prices = []
i = 0
for el in prices:
    prices[i] = "{:.2f}".format(el)
    price = str(int(el)) + str(" руб ") + str(prices[i].split('.')[1]) + str(" коп")
    new_prices.append(price)
    i += 1

print(prices)
print(new_prices)

y = 0
while y < len(new_prices) - 1:
    x = y + 1
    while x < len(new_prices):

        if int(new_prices[y].split()[0]) > int(new_prices[x].split()[0]):
            new_prices[y], new_prices[x] = new_prices[x], new_prices[y]
        elif int(new_prices[y].split()[0]) == int(new_prices[x].split()[0]):
            if int(new_prices[y].split()[2]) > int(new_prices[x].split()[2]):
                new_prices[y], new_prices[x] = new_prices[x], new_prices[y]
        else:
            x += 1
    y += 1

print(new_prices)

desc_new_prices = new_prices[::-1]
print(desc_new_prices)

print(f"Список 5 самых дорогих товаров:")
for idx, prc in enumerate(desc_new_prices[:5], start=1):
    print(f"№ {idx}.  {prc}")