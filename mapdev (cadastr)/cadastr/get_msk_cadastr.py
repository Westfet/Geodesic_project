import json
import re


# Функция для извлечения числовой части из строки
def extract_number(s):
    match = re.search(r'-(\d+) зона (\d+)', s)
    if match:
        return int(match.group(1)), int(match.group(2))
    match = re.search(r'-(\d+)', s)
    if match:
        return int(match.group(1)), 0
    return float('inf'), 0


# Функция для сортировки ключей
def key_sort(key):
    parts = key.split()
    return extract_number(key), int(parts[-1])


# Открываем JSON-файл и загружаем его
with open('../full_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Создаем словарь sc_to_cad_nom и cad_nom_to_sc
sc_to_cad_nom = {item["sc"]: [] for item in data}
cad_nom_to_sc = {item["cad_nom"]: item["sc"] for item in data}

# Сортируем ключи в обоих словарях
sc_keys = sorted(sc_to_cad_nom.keys(), key=key_sort)
cad_nom_keys = sorted(cad_nom_to_sc.keys(), key=key_sort)

# Заполняем словарь sc_to_cad_nom
for item in data:
    sc = item["sc"]
    cad_nom = item["cad_nom"]
    if cad_nom in cad_nom_to_sc:
        sc_to_cad_nom[cad_nom_to_sc[cad_nom]].append(cad_nom)

# Сохраняем результаты в новый JSON-файл
result_data = {
    "sc_to_cad_nom": sc_to_cad_nom,
    "cad_nom_to_sc": cad_nom_to_sc
}

with open('sorting/1.json', 'w', encoding='utf-8') as result_file:
    json.dump(result_data, result_file, ensure_ascii=False, indent=4)

print("Результат сохранен в 1.json")
