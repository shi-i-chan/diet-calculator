import os
import pandas as pd
from tqdm import tqdm

import parser_utils
import parser_config

from bs4 import BeautifulSoup as bs
from typing import List, Tuple, NoReturn


products_fn = parser_config.products_data_fn


def get_tabular_data(soup: bs) -> Tuple[List, List]:
	""" Get nutrients and weights from soup """
	tbl_titles = soup.findAll('td', attrs={'class': 'tbl-name'})
	tbl_values = soup.findAll('td', attrs={'class': 'tbl-value'})
	titles = [name.text.strip() for name in tbl_titles]
	values = [value.text.strip() for value in tbl_values]
	return values, titles


def get_ash_water(soup: bs) -> Tuple[List, List]:
	""" Get product water and ash from soup """
	all_spans = soup.findAll('span', attrs={'class': 'him_bx__legend pr__fl'})
	result = {}
	for span in all_spans:
		text = span.text.strip()
		split = text.split(' ')

		if split[0] == 'вода':
			split[-1] = split[-1].replace(',', '').replace('.', '')
			result['вода'] = ' '.join(split[2:])
		elif split[0] == 'зола':
			split[-1] = split[-1].replace(',', '').replace('.', '')
			result['зола'] = ' '.join(split[2:])
	return list(result.values()), list(result.keys())


def get_additions(soup: bs) -> Tuple[List, List]:
	""" Get product additional things from soup """
	p = soup.find('p', attrs={'class': 'pr__brick pr__ind_c pr__ind_c_mtop pr__brd_b pr__ind_endline'})

	titles = []
	all_a = p.findAll('a')
	for a in all_a:
		titles.append(a.text)

	values = []
	all_spans = p.findAll('span')
	for span in all_spans:
		values.append(span.text)

	if len(titles) == len(values):
		pass
	else:
		raise Exception('Problem with additions...')
	return values, titles


def get_calories(soup: bs) -> Tuple[List, List]:
	""" Get product calories from soup """
	all_spans = soup.findAll('span', attrs={'class': 'js__msr_cc'})
	kk = float(all_spans[2].text.split()[0].replace(',', '.'))
	return [kk], ['кКал']


def get_amino(product_id: int) -> Tuple[List, List]:
	""" Get product amino from product id """
	amino_url = parser_config.def_url + str(product_id) + '/amino'
	if soup := parser_utils.get_soup(amino_url):
		return get_tabular_data(soup)
	else:
		raise Exception('Problems with reading amino page.')


def get_product_data(product: str, product_id: int) -> pd.DataFrame:
	""" Get all product nutrients """
	url = parser_config.def_url + str(product_id)
	values, titles = get_amino(product_id)
	if soup := parser_utils.get_soup(url):
		for method in [get_tabular_data, get_ash_water, get_additions, get_calories]:
			result = method(soup)
			values += result[0]
			titles += result[1]
		return pd.DataFrame(values, columns=[product], index=titles)
	else:
		raise Exception('Problems with reading main page.')


def get_new_products_df(exist_products: List[str]) -> pd.DataFrame:
	""" Get new products dataframes """
	all_products = list(parser_config.products_dict.keys())
	new_products = [product for product in all_products if product not in exist_products]
	new_products_dfs = []
	for product in tqdm(new_products):
		if product not in exist_products:
			new_product_df = get_product_data(product, parser_config.products_dict[product])
			new_products_dfs.append(new_product_df)
	return pd.concat(new_products_dfs, axis=1)


def update_products_table() -> NoReturn:
	old_df = pd.read_excel(products_fn, index_col=0) if os.path.isfile(products_fn) else pd.DataFrame()
	exist_products = old_df.columns.tolist()
	new_products_df = get_new_products_df(exist_products)

	if new_products_df.shape[0] > 0:
		new_products_list = new_products_df.columns.tolist()

		# idk, it fixes some bug
		new_products_df.to_excel('temp_table.xlsx')
		new_products_df = pd.read_excel('temp_table.xlsx', index_col=0)
		os.remove('temp_table.xlsx')
		new_products_df = new_products_df.dropna()

		new_products_df = new_products_df.applymap(parser_utils.convert_weights)
		new_products_df = pd.concat([old_df, new_products_df], axis=1).reindex(parser_config.nutrients)
		new_products_df.to_excel(parser_config.products_data_fn)
		print('Add new products: ', new_products_list)
	else:
		print('There is no new products.')


update_products_table()
