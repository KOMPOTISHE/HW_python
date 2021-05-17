my_prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]


for i in my_prices:
    rub = f"{i // 1:.0f}"
    kop = f"{((i % 1)*100):.0f}"
    print(f"{rub}руб {kop.rjust(2, '0')}коп",end=", ")


print(id(my_prices))
my_prices.sort()
print(id(my_prices))
print(my_prices)
print(sorted(sorted(my_prices, reverse=True)[:5]))


prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
prices_s = sorted(prices, reverse=True)
print(prices_s)