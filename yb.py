import click
import pandas as pd
from lib.yahoobuy import YahooBuy
from lib import dfutil

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

yb = YahooBuy()

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def main():
    pass


@main.command()
def show_category_mapping():
    rs = []
    mapping = yb.mapping
    print(mapping)

@main.command()
@click.option('--cat_id', default=None, help='Crawl Yahoo Buy with specified \
category id.  If not specified, it will crawl all category and sub category ids')
@click.option('--filename', default='default', help='Specify the filename to save \
crawled result.  If not specified, name "default" will be used')
@click.option('--filetype', default='xlsx', type=click.Choice(['xlsx', 'csv']), 
    help='specify file type to save.  default to xlsx if not specified') 

def crawl(cat_id, filename, filetype):
    cat_ids = [ cat_id ]
    if cat_id is None:
        cat_ids = None
    rs = yb.crawl(cat_ids=cat_ids)
    df = pd.DataFrame(rs)
    print('writting result to output/{}.{}'.format(filename, filetype))
    if filetype == 'xlsx':
        df.to_excel('output/{}.xlsx'.format(filename), index=False)
    if filetype == 'csv':    
        df.to_csv('output/{}.csv'.format(filename), index=False)



@main.command()
@click.option('--filename', default='default', help='Specify the filename for \
crawled result used for query.  If not specified, name "default" will be used')
@click.option('--filetype', default='xlsx', type=click.Choice(['xlsx', 'csv']), 
    help='Specify file type to query from.  Default to xlsx if not specified') 

@click.option('--min_price', default=0, help='Minimun price to consider, Default to 0')
@click.option('--max_price', default=None, help='Maxmun price to consider, Default to no limit')
@click.option('--stats_view', is_flag=True, help='Show aggregated result grouped \
by category instead of raw data.  Default to show product count and average price \
for each category')

def query(filename, filetype, min_price, max_price, stats_view):
    if max_price is None:
        max_price = float('Inf')
    else:
        max_price = int(max_price)

    if filetype == 'xlsx':
        df = pd.read_excel('output/{}.xlsx'.format(filename))
    if filetype == 'csv':    
        df = pd.read_csv('output/{}.csv'.format(filename))

    df = df[df.price >= min_price]    
    df = df[df.price <= max_price]    
    if stats_view:
        df = dfutil.get_groupby_stats(df, ['category_id', 'category'], agg={'product_name':['count'], 'price':['mean']})

    print(df)

if __name__ == '__main__':
    main()

