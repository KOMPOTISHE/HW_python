class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        pass

        while True:
            try:
                val = int(input("Введите число: "))
                self.my_list.append(val)
                print(f"Текущий список - {self.my_list} \n ")
            except:
                print(f"недопустимое значение")
                y_or_n = input(f"Хотите попробовать еще раз? Y/N")

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else: return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())