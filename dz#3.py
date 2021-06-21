def thesaurus(*name):
    dct_name = {}

    for i in name:
        dct_name.setdefault(i[0], [])
        dct_name[i[0]].append(i)

    dct_name = dict(sorted(dct_name.items()))
    return dct_name

names = ['пртр', 'олег', 'ппкк', 'олцувау', 'цвцвц', 'вцвцвцв', 'вцввйцв', 'цвцвцв', 'оеоено', 'океоео']
print(thesaurus(*names))
print(thesaurus('петр', 'олег', 'ппкк', 'олцувау', 'цвцвц', 'вцвцвцв', 'вцввйцв', 'цвцвцв', 'оеоено', 'океоео'))