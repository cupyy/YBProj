import pandas as pd
import re

def get_groupby_stats(df=None, groups=None, agg=None, column_names=None):
    '''
    return aggregated view based on groups and agg function specified
    '''
    if groups is None:
        groups = []
    if agg is None:
        agg = {}

    if df is None or df.empty:
        output_columns = groups
        for key, values in agg.items():
            output_columns += ['{}_{}'.format(key, value) for value in values]

        return pd.DataFrame(columns=output_columns)

    stats_df = df
    stats_df = df[groups + list(agg.keys())]

    stats_df = stats_df.groupby(
            groups
        ).agg(agg).reset_index()
    ########################################################################
    # if column names are given, use the given column names,
    # otherwize use default column names
    ########################################################################
    stats_df = merge_col_levels(stats_df, merge_str='_')
    if column_names:
        stats_df.columns = [ *stats_df.columns[0:len(groups)], *column_names]
    ########################################################################

    return stats_df


def merge_col_levels(df=pd.DataFrame(), merge_str='_' ):
    df.columns = df.columns.map(merge_str.join)
    df.columns = [ re.sub('{}$'.format(merge_str), '', col) for col in df.columns]
    return df
