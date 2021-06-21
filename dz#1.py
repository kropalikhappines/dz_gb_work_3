dict_num = {'one': 'один',  # Создаем словарь
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}

def num_translate(num):
    return dict_num.get(num) # Возвращаем перевод, при не удаче вернет NOne

while True:
    num = input()

    print(num_translate(num))