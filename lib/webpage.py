from lazy import lazy
from bs4 import BeautifulSoup as BS
import requests

def encode_str(string=''):
    return string.encode('utf-8', 'ignore').decode('utf-8')

class WebPage():
    '''
    wrapper for requests and BeautifulSoup module for eazy access
    '''
    def __init__(self, **kwargs):
        url = kwargs.get('url', None)
        self.url = encode_str(url)
        self.requests = requests


    def connect(self):
        try:
            return self.requests.get(self.url)
        except requests.exceptions.RequestException as e:
            return e


    @lazy
    def res(self):
        rs = self.connect()
        #return None if type(rs) is str else rs
        return rs
        

    @lazy
    def html(self) :
        return self.res.text if type(self.res) is not str else self.res

    @lazy
    def sp(self):
        return BS(self.html, 'html5lib')





