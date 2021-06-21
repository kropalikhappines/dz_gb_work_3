from random import choice, randrange

def get_jokes(quantity, repeat_num=False): # Количество, повтор
    jokes_output = [] # Основной список

    if repeat_num: # Повтор включен
        for i in range(quantity):
            jokes_draft = [] # Список черновик
            jokes_draft.append(nouns.pop(randrange(len(nouns)))) # Отрываем и сохраняем
            jokes_draft.append(adverbs.pop(randrange(len(adverbs))))
            jokes_draft.append(adjectives.pop(randrange(len(adjectives))))
            jokes_draft = ' '.join(jokes_draft)
            jokes_output.append(jokes_draft)
    else:
        for i in range(quantity):
            jokes_draft = []
            jokes_draft.append(choice(nouns))
            jokes_draft.append(choice(adverbs))
            jokes_draft.append(choice(adjectives))
            jokes_draft = ' '.join(jokes_draft)
            jokes_output.append(jokes_draft)

    print(jokes_output)

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

get_jokes(9)
get_jokes(3, True)
get_jokes(2, True)
