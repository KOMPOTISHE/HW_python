with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    all_str = file.read().split('\n')
    my_gen = (i.split() for i in all_str)
    result = [tuple([el[0], el[5], el[6]]) for el in my_gen for m in el]
    print(result)