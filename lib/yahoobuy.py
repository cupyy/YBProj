from .WebPage.YahooBuy import Base 
from .WebPage.YahooBuy.sitemap import SiteMap
from .WebPage.YahooBuy.subcategory import SubCategory
from .WebPage.YahooBuy.category import Category
from .WebPage.YahooBuy.item import Item
from .webpage import WebPage
from lazy import lazy
from collections import OrderedDict

class YahooBuy():
    def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        self.base_url = 'https://tw.buy.yahoo.com'
        self.site_map_sub_url = 'help/helper.asp?p=sitemap&hpp=sitemap'
        self.cat_query_key = 'z'
        self.sub_query_key = 'sub'
        self.menucat_id = 'cl-menucate'
        self.hotrank_id = 'cl-hotrank'
        self.hotitem_id_keyword = 'rank'
        self.item_spec_class = 'item-spec'

    @lazy
    def sm(self):
        '''
        Yahoo Buy site map obj
        '''
        return SiteMap(
            sub_url=self.site_map_sub_url,
            cat_query_key = self.cat_query_key,
            sub_query_key = self.sub_query_key,
        )

    @lazy
    def mapping(self):
        return self.sm.mapping


    @lazy
    def sub_ids(self):
        '''
        return sub category id list
        '''
        return self.sm.sub_category_ids


    @lazy
    def cat_ids(self):
        '''
        return category id list
        '''
        return self.sm.category_ids


    def get_sub(self, id=None):
        return SubCategory(
            query_key=self.sub_query_key, 
            id=id
        )

    def get_cat(self, id=None):
        return Category(
            query_key=self.cat_query_key, 
            id=id
        )

    def get_item(self, url=None):
        return Item(
            url=url
        )

    def get_items_info(self, cat=None, sub=None, items=None, source=None):    
        rs = []
        for item in items:
            if not item.is_item:
                continue

            item_info = self.gen_item_info(
                cat=cat, item=item, source=source, sub=sub,
            )
            rs.append(item_info)
        return rs    


    def gen_item_info(self, cat=None, item=None, source=None, sub=None):    
        if sub is not None:
            sub_title = sub.title
        else:
            sub_title = item.title
        return OrderedDict({
            'category_id': cat.id,
            'category': cat.title,
            'sub_category': sub_title,
            'product_name': item.name,
            'price': item.price,
            #'source': source
        })


    def crawl(self, cat_ids=None):    
        if cat_ids is None:
            cat_ids = list(self.mapping.keys())

        rs = []
        for cat_id in cat_ids:
            print ('process category {} hot item'.format(cat_id))
            cat = self.get_cat(cat_id)
            rs += self.get_items_info(
                    cat=cat, items=cat.hot_items, source='category')

            for sub_id in self.mapping[cat_id]:
                print ('process sub category {} hot item'.format(sub_id))
                sub = self.get_sub(sub_id)
                rs += self.get_items_info(
                        cat=cat, items=sub.hot_items, source='sub_category', sub=sub)

        return rs        









