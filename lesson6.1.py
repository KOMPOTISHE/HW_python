from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        all_lst = zip_longest((' '.join(user.split(',')) for user in users), hobby, fillvalue=None)
        my_dict = dict((rows[0], rows[1]) for rows in all_lst)
        with open('merge', 'w', encoding='utf-8') as result:
            print(my_dict)