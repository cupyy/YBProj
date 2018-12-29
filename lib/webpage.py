from lazy import lazy
from bs4 import BeautifulSoup as BS
import requests
#import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


# https://dev.to/ssbozy/python-requests-with-retries-4p03
# exception handle
def requests_retry_session(
    retries=10,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

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
#         try:
#             return self.requests.get(self.url)
#         except Exception as e:
#             return e
        try:
            response = requests_retry_session().get(self.url)
        except Exception as x:
            print('connection failed: {} retrying...'.format( x.__class__.__name__))
#         else: 
#             #print('retry success', response.status_code)
        finally:
            pass

        return response





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





