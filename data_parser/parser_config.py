norm_data_fn = 'data/norm_data.xlsx'
products_data_fn = 'data/products_data.xlsx'

def_url = 'https://fitaudit.ru/food/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}

products_dict = {
    'Рис длиннозернистый': 158884,
    'Куриная грудка запеченная': 104790,
    'Помидоры свежие': 121036,
    'Шоколад темный 70 - 85': 146261,
    'Брокколи': 120729,
    'Яйцо куриное варёное': 190836,
    'Хлеб ржаной': 141639,
    'Скумбрия солёная': 336889,
    'Кефир': 190316,
    'Крупа ячневая': 157561,
    'Каша овсяная': 111812,
    'Морковь вареная': 120824,
    'Сыр Пармезан': 190548,
}

norm_dict = {
    'Белки': '75 г',
    'Жиры': '84 г',
    'Углеводы': '310 г',
    'Кальций': '1 000 мг',
    'Железо': '10 мг',
    'Магний': '400 мг',
    'Фосфор': '700 мг',
    'Калий': '4 700 мг',
    'Натрий': '1 300 мг',
    'Цинк': '11 мг',
    'Медь': '0,9 мг',
    'Марганец': '2,3 мг',
    'Селен': '55 мкг',
    'Фтор': '4 000 мкг',
    'Витамин A': '900 мкг',
    'Бета-каротин': '5 000 мкг',
    'Альфа-каротин': '5 000 мкг',
    'Витамин D': '15 мкг',
    'Витамин D2': '7,5 мкг',
    'Витамин D3': '16,25 мкг',
    'Витамин E': '14,6 мг',
    'Витамин K': '120 мкг',
    'Витамин C': '90 мг',
    'Витамин B1': '1,2 мг',
    'Витамин B2': '1,3 мг',
    'Витамин B3': '16 мг',
    'Витамин B4': '500 мг',
    'Витамин B5': '5 мг',
    'Витамин B6': '1,3 мг',
    'Витамин B9': '400 мкг',
    'Витамин B12': '2,4 мкг',
    'Триптофан': '0,8 г',
    'Треонин': '2,4 г',
    'Изолейцин': '2 г',
    'Лейцин': '4,6 г',
    'Лизин': '4,1 г',
    'Метионин': '1,8 г',
    'Цистин': '1,8 г',
    'Фенилаланин': '4,4 г',
    'Тирозин': '4,4 г',
    'Валин': '2,5 г',
    'Аргинин': '6,1 г',
    'Гистидин': '2,1 г',
    'Аланин': '6,6 г',
    'Аспарагиновая': '12,2 г',
    'Глутаминовая': '13,6 г',
    'Глицин': '3,5 г',
    'Пролин': '4,5 г',
    'Серин': '8,3 г',
    'крахмала': '400 г',
    'клетчатки': '30 г',
    'холестерина': '250 мг',
    'сахаров': '50 г',
    'трансжиров': '2 г',
    'кКал': 2500,
    'вода': 2500,
    'зола': 100,
}

main = [
    'Белки',
    'Жиры',
    'Углеводы',
]

vitamins = [
    'Витамин A',
    'Бета-каротин',
    'Альфа-каротин',
    'Витамин D',
    'Витамин D2',
    'Витамин D3',
    'Витамин E',
    'Витамин K',
    'Витамин C',
    'Витамин B1',
    'Витамин B2',
    'Витамин B3',
    'Витамин B4',
    'Витамин B5',
    'Витамин B6',
    'Витамин B9',
    'Витамин B12',
]

minerals = [
    'Кальций',
    'Железо',
    'Магний',
    'Фосфор',
    'Калий',
    'Натрий',
    'Цинк',
    'Медь',
    'Марганец',
    'Селен',
    'Фтор',
]

aminos = [
    'Триптофан',
    'Треонин',
    'Изолейцин',
    'Лейцин',
    'Лизин',
    'Метионин',
    'Цистин',
    'Фенилаланин',
    'Тирозин',
    'Валин',
    'Аргинин',
    'Гистидин',
    'Аланин',
    'Аспарагиновая',
    'Глутаминовая',
    'Глицин',
    'Пролин',
    'Серин',
]

other = [
    'крахмала',
    'клетчатки',
    'холестерина',
    'сахаров',
    'трансжиров',
    'кКал',
    'вода',
    'зола',
]

nutrients = main + vitamins + minerals + aminos + other
