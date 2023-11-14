import requests
from bs4 import BeautifulSoup


def parse_page(page_number):
    url = f'https://terraingis.ru/msk-{page_number:02}.html'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        proj_strings_list = [tag.get_text() for tag in soup.find_all('span') if
                             tag.get_text().startswith('+terraingis_mapbasic (proj)')]
        proj_strings_list = ['+axis=neu ' + text for text in proj_strings_list]

        msk_elements = soup.find_all('div',
                                     class_='expert-review-faq-item__question js-expert-review-faq-item-question')
        msk_list = [element.get_text() for element in msk_elements if
                    element.get_text().startswith('МСК')]

        micro_dict = {msk: proj_string for msk, proj_string in zip(msk_list, proj_strings_list)}
        return micro_dict
    else:
        return None


def main():
    main_dict = {}
    excluded_pages = []
    for page_number in range(1, 91):
        micro_dict = parse_page(page_number)
        if not micro_dict:
            excluded_pages.append(page_number)
            continue
        main_dict.update(micro_dict)
    # for key, value in main_dict.items():
    #    print(f'{key} : {value}')
    # print(f'Не хватает регионов: {excluded_pages}')
    return main_dict


if __name__ == "__main__":
    main()
