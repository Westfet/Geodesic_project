import requests
from bs4 import BeautifulSoup
import re
import json


def parse_msk_page(url):
    page_number = int(re.search(r'\d+', url).group())  # Извлекаем номер страницы из url

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        code_elements = soup.find_all('code')

        msk_name_strings = []
        proj_strings = []

        for code_element in code_elements:
            code_lines = code_element.get_text().split('\n')
            if code_lines and not code_lines[0].strip():
                del code_lines[0]

            for line in code_lines:
                matches = re.findall(r'"([^"]*)"', line)
                msk_name = matches[0]
                if not msk_name.startswith('МСК'):
                    msk_name = f'МСК-{page_number} ' + msk_name
                msk_name_strings.append(msk_name)
                splitted_string = line.split(', ')
                new_string = f'+axis=neu +proj=tmerc +lat_0={splitted_string[5]} +lon_0={splitted_string[4]} ' \
                             f'+k=1 +x_0={splitted_string[-2]} +y_0={splitted_string[-1]} ' \
                             f'+ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs'
                proj_strings.append(new_string)

        result_dict = dict(zip(msk_name_strings, proj_strings))

        return result_dict

    else:
        print(f'Ошибка {response.status_code}: Невозможно получить страницу.')
        return {}


def main():
    page_numbers = [49]
    main_dict = {}

    for page_number in page_numbers:
        url = f'https://mapbasic.ru/msk{page_number}'
        micro_dict = parse_msk_page(url)
        main_dict.update(micro_dict)
    # for key, value in main_dict.items():
    #    print(f'{key} : {value}')
    with open('inspect_msk2.json', 'w', encoding='utf-8') as result_file:
        json.dump(main_dict, result_file, ensure_ascii=False, indent=4)
    return main_dict


if __name__ == "__main__":
    main()
