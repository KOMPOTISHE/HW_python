my_dict = {"zero": "ноль", "one": "один", "tow": "два", "three": "три", "four": "четыре", "five": "пять",
           "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}



def num_translate(word):
    return my_dict.get(word)


user = input("Enter: ")
print(num_translate(user))

