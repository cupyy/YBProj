from lib.WebPage import Base as WBase
from lazy import lazy

class Base(WBase):
    base_url = 'https://tw.buy.yahoo.com'
    def __init__(self, **kwargs):
        self.sub_url = kwargs.get('sub_url', None)
        if 'url' not in kwargs:
            kwargs['url'] = '{}/{}'.format(self.base_url, self.sub_url)

        super().__init__(**kwargs)
        self.menucat_id = kwargs.get('menucat_id', 'cl-menucate')
        self.menucat_title_class = kwargs.get('menucat_title_class', 'title')
        self.hotrank_id = kwargs.get('hotrank_id', 'cl-hotrank')
        self.hotitem_id_keyword = kwargs.get('hotitem_id_keyword', 'rank')


    @lazy
    def menucat(self):
        return self.sp.find('div', {'id':self.menucat_id})


    @lazy
    def title(self):
        return self.menucat.find('', {'class':self.menucat_title_class}).text


    @lazy    
    def all_links(self):
        return self.sp.find_all('a')

    @lazy
    def all_hrefs(self):
        rs = []
        for link in self.all_links:
            try:
                rs.append(link['href'])
            except:
                pass
        return rs

    @lazy
    def has_ranking(self):
        if self.hot_rank:
            return True

        return False

    @lazy 
    def hot_rank(self):
        return self.sp.find('', id=lambda x: x is not None and x == self.hotrank_id)

    @lazy    
    def ranks(self):
        return self.hot_rank.find_all('', id=lambda x: x is not None and self.hotitem_id_keyword in x)


