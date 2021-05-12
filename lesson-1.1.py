duration = int(input("введите кол-во секунд: "))
s = duration % 60
m = (duration // 60) % 60
h = (duration // 3600) % 60

print(h,"час", m,"минут", s, "секунд")
