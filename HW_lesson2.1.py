basic_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
for i in range(len(basic_list)):
    i += index
    if basic_list[i][-1].isdigit():
        if basic_list[i][0] in '+-':
            basic_list[i] = f'{basic_list[i][0]}{int(basic_list[i]):02}'
        else:
            basic_list[i] = f'{int(basic_list[i]):02}'
        basic_list.insert(i, '"')
        basic_list.insert(i + 2, '" ')
        index += 2
    else:
        basic_list[i] = f'{basic_list[i]} '


print(basic_list)
print(''.join(basic_list))
