from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n):
    for i in range(n):
        random_index = choice(nouns)
        random_index_1 = choice(adverbs)
        random_index_2 = choice(adjectives)
        joke = f'{random_index} {random_index_1} {random_index_2}'
        print(joke)





get_jokes(n=3)