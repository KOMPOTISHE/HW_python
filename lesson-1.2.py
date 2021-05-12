cube_number_list = [i ** 3 for i in range(1, 1001, 2)]
total = 0

for number in cube_number_list:
    digit_sum = 0
    temp_number = number

    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number //= 10

    if digit_sum % 7 == 0:
        total += number

print(total)

cube_number_list1 = [(i ** 3) + 17 for i in range(1, 1001, 2)]
total2 = 0

for number in cube_number_list1:
    digit_sum = 0
    temp_number = number

    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number //= 10

    if digit_sum % 7 == 0:
        total2 += number

print(total2)

