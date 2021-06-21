from random import choice, randrange

def repeat(a, b):
    a.append(b.pop(randrange(len(b)))) #функция добавления, длина списка

def infinity(c, d): # функция добавления для генерирования бесконечности
    c.append(choice(d))

def app(x, r): # функция добавления
    x = ' '.join(x)
    r.append(x)

def get_jokes(quantity, repeat_num=False): # Количество, повтор по умолчанию выключен
    jokes_output = [] # Основной список

    if repeat_num: # Повтор включен
        for i in range(quantity):
            jokes_draft = [] # Список черновик
            repeat(jokes_draft, nouns) # функция добавления, длина списка
            repeat(jokes_draft, adverbs)
            repeat(jokes_draft, adjectives)
            app(jokes_draft,jokes_output)

    else:
        for i in range(quantity):
            jokes_draft = []
            infinity(jokes_draft, nouns)
            infinity(jokes_draft, adverbs)
            infinity(jokes_draft, adjectives)
            app(jokes_draft,jokes_output)

    print(jokes_output)

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

get_jokes(9)
get_jokes(3, True)
get_jokes(2, True)
