import click
import pandas as pd
from lib.yahoobuy import YahooBuy


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

yb = YahooBuy()

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def main():
    pass


@main.command()
#@click.option('--all', is_flag=True, help='sync all')
def show_category_mapping():
    rs = []
    mapping = yb.mapping
    print(mapping)
#     for cat_id, sub_ids in mapping.items():
#         for sub_id in sub_ids:
#             rs.append({
#                 'category_id': cat_id,
#                 'sub_category_id': sub_id
#             })
# 
#     print(pd.DataFrame(rs))

@main.command()
@click.option('--cat_id', default=None, help='Crawl Yahoo Buy with specified \
category id.  if not specified, it will crawl all category ids')
@click.option('--filename', default='default', help='specify the filename to save \
crawled result.  if not specified, name "default" will be used')
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
@click.option('--filename', default='default', help='specify the filename for \
crawled result used for query if not specified, name "default" will be used')
@click.option('--filetype', default='xlsx', type=click.Choice(['xlsx', 'csv']), 
    help='specify file type to query from.  default to xlsx if not specified') 

@click.option('--min_price', default=0, help='minimun price to show, default to 0')
@click.option('--max_price', default=None, help='maxmun price to show, default to no limit')
def query(filename, filetype, min_price, max_price):
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
    print(df)

if __name__ == '__main__':
    main()

