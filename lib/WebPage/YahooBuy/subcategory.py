from lib.WebPage.YahooBuy import Base 
from lazy import lazy
from collections import OrderedDict
from lib.WebPage.YahooBuy.item import Item

class SubCategory(Base):
    '''
    web page object for sub category id url (i.e https://tw.buy.yahoo.com/?sub=10)
    '''
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.query_key = kwargs.get('query_key', 'sub')
        kwargs['sub_url'] = '?{}={}'.format(self.query_key, self.id)
        super().__init__(**kwargs)


    @lazy
    def hot_items(self):
        '''
        return hot items within this web page object
        '''
        if not self.has_ranking:
            return []

        return [ Item(url=rank.find('a')['href']) for rank in self.ranks ]







