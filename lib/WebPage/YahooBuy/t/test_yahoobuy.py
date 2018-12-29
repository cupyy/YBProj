import unittest
from unittest import mock
import dfutil, util
import numpy as np
import pandas as pd
import datetime
from WebPage.YahooBuy.yahoobuy import YahooBuy
from collections import OrderedDict
from itertools import product
import os
from logger import Logger

logger = Logger()

#assertEqual/True/False/Raises
#https://www.mattcrampton.com/blog/a_list_of_all_python_assert_methods/

def setUpModule():
    logger.logit('setUpModule')

def tearDownModule():
    logger.logit('tearDownModule')

class YahooBuyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.logit('setUpClass {}'.format(cls.__name__))

    @classmethod
    def tearDownClass(cls):
        logger.logit('tearDownClass {}'.format(cls.__name__))

    def setUp(self):
        self.yb = YahooBuy()
        logger.logit ('setUp {}'.format(self._testMethodName))

    def tearDown(self):
        logger.logit ('tearDown {}'.format(self._testMethodName))

#     def test_sm(self):    
#         sm = self.yb.sm
#         self.assertEqual(sm.sub_url, 'help/helper.asp?p=sitemap&hpp=sitemap')
#         sub_ids = sm.sub_category_ids
#         sm.category_ids
#         pass


    def test_yb(self):
        sm = self.yb.sm
        zones = sm.zones
        mapping = sm.mapping
        rs = []
        limit = 0 
        index = 0

        import pdb; pdb.set_trace()
        #rs = self.yb.crawl(cat_ids=['40'])
        rs = self.yb.crawl()

    
        df = pd.DataFrame(rs)
        df.to_excel('/Users/yangyining/yb_test.xlsx')    

#         zone_info = sm.get_zone_info(zone=zones[0])
#         cat_ids = self.yb.cat_ids
#         self.assertNotEqual(len(cat_ids), 0)
#         sub_ids = self.yb.sub_ids
#         self.assertNotEqual(len(sub_ids), 0)
#         import pdb; pdb.set_trace()
#         cat = self.yb.get_cat(cat_ids[0])
#         sub = self.yb.get_sub(sub_ids[0])
# 
#         href = cat.ranks[2].find('a')['href']
#         item = self.yb.get_item(url=href)

        pass
    
