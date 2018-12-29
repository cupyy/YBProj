from lib.WebPage.YahooBuy import Base 
from lazy import lazy
from collections import OrderedDict

class Item(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mainitem_id = kwargs.get('mainitem_id', 'cl-mainitem')
        self.spec_class = kwargs.get('spec_class', 'item-spec')
        self.name_class = kwargs.get('name_class', 'title')
        self.price_tag = kwargs.get('price_tag', 'span')
        self.price_class = kwargs.get('price_class', 'price')

    @lazy
    def is_item(self):
        '''
        sometimes the referenced url is not item format
        i.e https://tw.buy.yahoo.com/?catitemid=116232
        '''
        if self.mainitem:
            return True

        return False

    @lazy
    def mainitem(self):
        '''
        return mainitem html obj if exists
        '''
        try:
            return self.sp.find('div', {'id':self.mainitem_id})
        except:
            return None

    @lazy
    def spec(self):
        '''
        return item spec html obj
        '''
        return self.mainitem.find('div', {'class':self.spec_class})

    @lazy
    def name(self):
        '''
        item product name
        '''
        return self.spec.find('div', {'class':self.name_class}).text


    @lazy
    def price(self):
        '''
        item price
        '''
        text = self.spec.find(self.price_tag, {'class': self.price_class}).text
        text = text.replace('$','').replace(',','')
        return int(text)


