import unittest
from unittest import mock
import dfutil, util
import numpy as np
import pandas as pd
import datetime
from WebPage.YahooBuy.subcategory import SubCategory
from WebPage.YahooBuy.sitemap import SiteMap
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

class SiteMapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.logit('setUpClass {}'.format(cls.__name__))

    @classmethod
    def tearDownClass(cls):
        logger.logit('tearDownClass {}'.format(cls.__name__))

    def setUp(self):
        logger.logit ('setUp {}'.format(self._testMethodName))

    def tearDown(self):
        logger.logit ('tearDown {}'.format(self._testMethodName))


    def test_1(self):
        import pdb; pdb.set_trace()
        sm = SiteMap()
        sub_ids = sm.sub_category_ids
        for sub_id in sub_ids:
            sub = SubCategory(id=sub_id)
            print ('id: {} has_ranking: {}'.format(sub_id, sub.has_ranking))

        import pdb; pdb.set_trace()
        title = sub.title

        pass
    
