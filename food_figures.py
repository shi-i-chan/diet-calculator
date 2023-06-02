import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from data_parser import parser_config
from board_utils import get_colors_dict

from typing import List, NoReturn, Tuple


def get_percent_nutrients_df(diet: dict, norm_factor: int = 1) -> pd.DataFrame:
    """ Convert products table from grams to daily norm percent """
    norm_df = pd.read_excel(f'data_parser/{parser_config.norm_data_fn}', index_col=0)
    products_data = pd.read_excel(f'data_parser/{parser_config.products_data_fn}', index_col=0)

    products = list(diet.keys())
    sub_df = products_data[products]
    for product in products:
        weight = diet[product]
        factor = weight / 100
        sub_df[product] = sub_df[product] * factor
    pct_df = sub_df.div((norm_df * norm_factor)['Norm'], axis=0) * 100
    pct_df = pct_df.reindex(parser_config.nutrients)
    return pct_df


def get_daily_price_df(price_dict: dict, diet_dict: dict) -> pd.DataFrame:
    """ Generate daily price df """
    data = {}
    for product, weight in diet_dict.items():
        w_kg = weight / 1000
        if product in price_dict:
            data[product] = w_kg * price_dict[product]
        else:
            print("Some problems with ", product)
    costs_df = pd.DataFrame(data=data, index=['price'])
    return costs_df


def plot_prices(fig: go.Figure, prices_df: pd.DataFrame, colors_dict: dict,
                row: int = 1, col: int = 1, price_factor: int = 1,
                visible: bool = True) -> NoReturn:
    """ Plot price chart """
    prices_df = prices_df * price_factor
    sorted_cols = prices_df.sum().sort_values(ascending=False).index
    prices_df = prices_df[sorted_cols]
    for idx, product in enumerate(sorted_cols):
        fig.add_trace(go.Bar(x=[product] if visible else [idx],
                             y=prices_df[product],
                             name=product,
                             legendgroup=product,
                             showlegend=False,
                             marker_color=colors_dict[product],
                             ),
                      row=row,
                      col=col,
                      )
    if visible:
        price_df_sum = prices_df.sum(axis=0)
        fig.add_trace(
            go.Scatter(
                x=price_df_sum.index,
                y=price_df_sum.values.astype('int32'),
                text=price_df_sum.values.astype('int32'),
                mode='text',
                textposition='top center',
                textfont=dict(
                    size=13,
                ),
                showlegend=False
            ),
            row=row,
            col=col,
        )


def plot_nutrients(fig, nutrients_df, colors_dict: dict,
                   text_size: int = 13, tickangle: int = 50, tickfont_size: int = 13,
                   row: int = 1, col: int = 1, visible: bool = True) -> NoReturn:
    """ Plot nutrients chart """
    products = nutrients_df.columns
    index = nutrients_df.index
    for product in products:
        fig.add_trace(go.Bar(x=index,
                             y=nutrients_df[product],
                             name=product if visible else '',
                             offsetgroup=0,
                             legendgroup=product,
                             marker_color=colors_dict[product],
                             ),
                      row=row,
                      col=col,
                      )
    fig.add_trace(
        go.Scatter(
            x=nutrients_df.index,
            y=nutrients_df.sum(axis=1).values.astype('int32'),
            text=nutrients_df.sum(axis=1).values.astype('int32'),
            mode='text',
            textposition='top center',
            textfont=dict(
                size=text_size,
            ),
            showlegend=False
        ),
        row=row,
        col=col,
    )

    fig.add_hline(y=100, line_color='orange', row=row, col=col)

    fig.update_xaxes(
        tickangle=tickangle,
        showticklabels=True,
        tickfont_size=tickfont_size,
        row=row,
        col=col,
    )


def init_figure(rows: int = 1, cols: int = 1, specs: List = None, titles: Tuple = None) -> go.Figure:
    """ Init empty figure """
    fig = make_subplots(
        rows=rows, cols=cols,
        specs=specs,
        subplot_titles=titles,
    )
    return fig


def make_figure(products_data, price_data, visible: bool = True) -> go.Figure:
    """ Plot all data """
    nutrients_df = get_percent_nutrients_df(products_data)
    daily_price_df = get_daily_price_df(price_data, products_data)
    colors_dict = get_colors_dict(nutrients_df.columns)

    daily_costs = int(daily_price_df.sum(axis=1)[0]) if visible else ''

    figure_params = {
        'rows': 2,
        'cols': 2,
        'specs': [[{"colspan": 2}, None], [{}, {}]],
        'titles': ("Nutrients", f' Daily costs {daily_costs}',  f'Monthly costs {daily_costs*30}'),  # TODO
    }
    fig = init_figure(**figure_params)

    plot_nutrients(fig, nutrients_df, colors_dict, row=1, col=1, visible=visible)
    plot_prices(fig, daily_price_df, colors_dict, row=2, col=1, visible=visible)
    plot_prices(fig, daily_price_df, colors_dict, row=2, col=2, price_factor=30, visible=visible)

    fig.update_layout(
        barmode='stack',
        height=1000,
        # width=1100,
        title_text="Food calculator",
    )
    return fig
