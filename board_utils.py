import pandas as pd
import plotly.express as px
from dash import dcc, html, dash_table

from data_parser import parser_config
from default_data import default_diet, default_prices, default_weights

import dash
from typing import List, Tuple


products_list = pd.read_excel(f'data_parser/{parser_config.products_data_fn}', index_col=0).columns.tolist()


def table_to_dicts(table_data: List[dict]) -> Tuple[dict, dict]:
    """ Convert dataframe """
    products_data, price_data = {}, {}
    for row in table_data:
        product = row['title_col']
        weight = int(row['weight_col'])
        price = int(row['price_col'])
        products_data[product] = weight
        price_data[product] = price
    return products_data, price_data


def get_product_price(product: str) -> float:
    """ Get product price """
    if product in default_prices:
        return default_prices[product]
    return 0


def get_product_weight(product: str) -> float:
    """ Get product weight """
    if product in default_weights:
        return default_weights[product]
    return 0


def get_default_diet() -> List:
    """ Get default diet data """
    default_diet_table = []
    for product in get_default_diet_products():
        default_diet_table.append({'title_col': product,
                                   'weight_col': get_product_weight(product),
                                   'price_col': get_product_price(product)})
    return default_diet_table


def get_default_diet_products() -> List[str]:
    """ Get default diet products """
    products = list(default_diet.keys())
    return products


def clean_table(table_data, selected_products):
    for table_row in table_data:
        table_product = table_row['title_col']
        if table_product not in selected_products:
            table_data.remove(table_row)
    return table_data


def get_layout(app: dash) -> dash:
    """ Set layout to dash """
    app.layout = html.Div([
        dcc.Dropdown(options=products_list,
                     id='products_dropdown',
                     value=get_default_diet_products(),
                     multi=True,
                     ),
        html.Br(),
        dash_table.DataTable(
            id='table_id',
            columns=[{'name': 'Title',
                      'id': 'title_col',
                      'deletable': False,
                      'renamable': False},
                     {'name': 'Weight',
                      'id': 'weight_col',
                      'deletable': False,
                      'renamable': False},
                     {'name': 'Price',
                      'id': 'price_col',
                      'deletable': False,
                      'renamable': False}
                     ],
            data=get_default_diet(),
            editable=True
        ),
        dcc.Graph(id='graph'),
    ])
    return app


def get_colors_dict(keys: List[str]) -> dict:
    """ Get colors """
    colors = px.colors.qualitative.Dark24 + px.colors.qualitative.Alphabet  # + some to get more colors
    colors_dict = {}
    for idx, key in enumerate(keys):
        colors_dict[key] = colors[idx]
    return colors_dict
