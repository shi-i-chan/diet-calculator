import requests
from bs4 import BeautifulSoup as bs

from parser_config import headers

from typing import Union
from requests import Response


def get_html(url: str) -> Union[Response, bool]:
    """ Get html from url """
    with requests.Session() as s:
        page_html = s.get(url, headers=headers)
    if page_html.status_code == 200:
        return page_html
    return False


def get_soup(url: str) -> Union[bs, bool]:
    """ Get soup from url """
    if page_html := get_html(url):
        soup = bs(page_html.text, 'html.parser')
        return soup
    return False


def convert_weights(value: Union[int, float, str]) -> float:
    """ Convert weights to grams """
    if value == 'н/д':
            return 0
    elif isinstance(value, int):
            return value
    elif isinstance(value, float):
            return value
    else:
            split = value.split()
            if len(split) == 2 and split[1] == 'г':
                    return float(split[0].replace(',', '.'))

            elif len(split) == 2 and split[1] == 'мг':
                    return float(split[0].replace(',', '.')) / 1_000

            elif len(split) == 2 and split[1] == 'мкг':
                    return float(split[0].replace(',', '.')) / 1_000_000

            elif len(split) == 3 and split[2] == 'мг':
                    return (int(split[0]) * 1000 + float(split[1].replace(',', '.'))) / 1_000

            elif len(split) == 3 and split[2] == 'мкг':
                    return (int(split[0]) * 1000 + float(split[1].replace(',', '.'))) / 1_000_000
            else:
                    print("Value is: ", value)
                    raise Exception('Что-то пошло не так азазаза')
