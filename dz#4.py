def thesaurus_adv(*name_family):
    n_f_dct = {}
    
    for i in name_family:
        name, family = i.split()
        n_f_dct.setdefault(family[0], {}).setdefault(name[0], [])
        n_f_dct[family[0]][name[0]].append(i)

    n_f_dct = dict(sorted(n_f_dct.items()))

    return n_f_dct

name_family = ['Петр Алексеев', 'Иван Сергеев', 'Инна Серова', 'Илья Иванов', 'Анна Савельева', 'Нан Алек']
print(thesaurus_adv(*name_family))
