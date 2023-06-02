import pandas as pd

from parser_utils import convert_weights
from parser_config import norm_dict, norm_data_fn, nutrients

norm_df = pd.DataFrame(norm_dict.values(), index=list(norm_dict.keys()), columns=['Norm'])
norm_df = norm_df.applymap(convert_weights).reindex(nutrients)
norm_df.to_excel(norm_data_fn)
