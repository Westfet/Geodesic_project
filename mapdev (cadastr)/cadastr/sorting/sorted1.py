import json
import re

# Открываем JSON-файл и загружаем его
with open('../../full_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)


# Функция для извлечения числовой части из строки
def extract_number(s):
    match = re.search(r'-(\d+)', s)
    if match:
        return int(match.group(1))
    return float('inf')  # Если числовой части нет, ставим бесконечность


# Убираем значения "sc" равные None
data = [item for item in data if item["sc"] is not None]

# Сортируем данные на основе ключей
sorted_data = sorted(data, key=lambda x: (extract_number(x["sc"]), x["sc"]))

# Создаем словарь sc_to_cad_nom
sc_to_cad_nom = {item["sc"]: [] for item in sorted_data}

# Выводим результат
print(sc_to_cad_nom)

# Сохраняем результат в новый JSON-файл
with open('1.json', 'w', encoding='utf-8') as result_file:
    json.dump(sc_to_cad_nom, result_file, ensure_ascii=False, indent=4)

print("Результат сохранен в 1.json")
