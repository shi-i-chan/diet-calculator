import webbrowser
from threading import Timer
import plotly.graph_objects as go
from dash import Dash, Input, Output, State


import food_figures
from board_utils import get_layout, table_to_dicts, get_product_price, get_product_weight, clean_table

from typing import List, NoReturn

visible = True


def main():
    app = Dash(__name__)
    app = get_layout(app)

    @app.callback(
        Output('table_id', 'data'),
        Input('products_dropdown', 'value'),
        State('table_id', 'data'),
    )
    def add_product(selected_products: List[str], table_data: List[dict]) -> List[dict]:
        exist_products = [row['title_col'] for row in table_data]
        for product in selected_products:
            if product not in exist_products:
                table_data.append({'title_col': product,
                                   'weight_col': get_product_weight(product),
                                   'price_col': get_product_price(product)})
        table_data = clean_table(table_data, selected_products)
        return table_data

    @app.callback(
        Output('graph', 'figure'),
        Input('table_id', 'data'),
    )
    def plot_charts(table_data: List[dict]) -> go.Figure:
        return food_figures.make_figure(*table_to_dicts(table_data), visible=visible)
    return app


def open_browser() -> NoReturn:
    webbrowser.open_new("http://localhost:{}".format(port))


if __name__ == '__main__':
    app = main()

    port = 8050
    Timer(1, open_browser).start()
    app.run_server(debug=False, port=port, use_reloader=False)
    input('Press any key to exit...')
