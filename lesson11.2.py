class DivisionByNull(Exception):
    def __init__(self, txt):
        self.txt = txt

num = input("Введите делимое: ")
num_2 = input("Введите делитель: ")
try:
    num = int(num)
    num_2 = int(num_2)
    if num_2 == 0:
        raise DivisionByNull("На ноль делить не буду!!!")
except (ZeroDivisionError, DivisionByNull) as err:
    print(err)
else:
    print(num / num_2)