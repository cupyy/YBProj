from lib.WebPage.YahooBuy import Base 
from lazy import lazy
from collections import OrderedDict

class SiteMap(Base):
    def __init__(self, **kwargs):
        if 'sub_url' not in kwargs:
            kwargs['sub_url'] = 'help/helper.asp?p=sitemap&hpp=sitemap'
        super().__init__(**kwargs)
        self.cat_query_key = kwargs.get('cat_query_key', 'z')
        self.sub_query_key = kwargs.get('sub_query_key', 'sub')

        self.sitemap_id = kwargs.get('sitemap_id', 'cl-sitemap')
        self.zone_class = kwargs.get('zone_class', 'zone')
        self.zone_tag = kwargs.get('zone_tag', 'li')

    @lazy
    def content(self):
        return self.sp.find('div', {'id': self.sitemap_id}).find('div', {'class':'module'})

    @lazy
    def zones(self):
        return self.content.find_all(self.zone_tag, {'class': self.zone_class})


    def get_zone_info(self, zone=None):
        info = OrderedDict()
        cat_link = zone.find('a', href=lambda x: self.cat_query_key in x)
        sub_links = zone.find_all('a', href=lambda x: self.sub_query_key in x)
        if cat_link and sub_links:
            info['cat_id'] = cat_link['href'].split('=')[1]
            info['sub_ids'] = [ link['href'].split('=')[1] for link in sub_links ]
        return info

    @lazy
    def mapping(self):
        rs = OrderedDict()
        for zone in self.zones:
            info = self.get_zone_info(zone)
            if info:
                rs[info['cat_id']] = info['sub_ids']

        return rs    



    def get_refs(self, key=None):
        rs = []
        for href in self.all_hrefs:
            if href.startswith('/?{}='.format(key)):
                rs.append(href)

        return rs        


    @lazy
    def sub_category_refs(self):
        return self.get_refs(self.sub_query_key)


    @lazy
    def category_refs(self):
        return self.get_refs(self.cat_query_key)


    @lazy
    def sub_category_ids(self):
        return [ ref.split('=')[1] for ref in self.sub_category_refs ]


    @lazy
    def category_ids(self):
        return [ ref.split('=')[1] for ref in self.category_refs ]



