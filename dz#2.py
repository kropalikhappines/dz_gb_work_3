dict_num = {'one': 'один',
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
    res = dict_num.get(num.lower()) # переводим нижний регистр
    if num.istitle(): # Првоеряем заглавную букву
        return res.capitalize() # Возвращаем заглавную букву
    return res # Возвращаем маленькую букву

while True:
    num = input()

    print(num_translate(num))