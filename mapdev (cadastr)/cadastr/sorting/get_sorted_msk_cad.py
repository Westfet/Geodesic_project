import json

# Загрузим первый и второй словари из файлов
with open('1.json', 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)

with open('2.json', 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)

# Создадим словарь для объединенных данных
result_dict = {key: [] for key in data1}

# Пройдемся по второму словарю и добавим ключи в первый словарь
for key2, value2 in data2.items():
    if value2 in result_dict:
        result_dict[value2].append(key2)

# Сохраним объединенный словарь в файл
with open('../msk_cadastr.json', 'w', encoding='utf-8') as output_file:
    json.dump(result_dict, output_file, ensure_ascii=False, indent=4)
