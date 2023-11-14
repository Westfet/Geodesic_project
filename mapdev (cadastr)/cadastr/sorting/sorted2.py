import json

# Загрузка данных из JSON файла
with open('../../full_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создание второго словаря
sc_to_cad_nom = {}
for item in data:
    sc = item['sc']
    cad_nom = item['cad_nom']
    if sc and cad_nom:  # Проверка на пустые значения
        sc_to_cad_nom[cad_nom] = sc

# Сортировка второго словаря
sorted_sc_to_cad_nom = dict(sorted(sc_to_cad_nom.items(), key=lambda x: (int(x[0].split(':')[0]), int(x[0].split(':')[1]))))

# Сохранение второго словаря в JSON файл
with open('2.json', 'w', encoding='utf-8') as outfile:
    json.dump(sorted_sc_to_cad_nom, outfile, ensure_ascii=False, indent=4)
