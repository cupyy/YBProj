from lazy import lazy
from bs4 import BeautifulSoup as BS
import requests, itertools
from lxml.html import fromstring
#import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import ProxyError

# https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/#5-things-to-keep-in-mind-while-using-proxies-and-rotating-ip-addresses6
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


# https://dev.to/ssbozy/python-requests-with-retries-4p03
# https://www.peterbe.com/plog/best-practice-with-retries-with-requests
# network connection handle with retry
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
        self.timeout=kwargs.get('timeout', 3)
        self.retries=kwargs.get('retries', 10)
        ########################################################################
        # TODO possible proxy support in the future.  Currently not stable
        ########################################################################
        self.use_proxy=kwargs.get('use_proxy', False)
        ########################################################################
        self.url = encode_str(url)
        self.requests = requests

    @lazy
    def proxy_pool(self):
        return itertools.cycle(get_proxies())


    def connect(self, proxy=None):
        params = {
            'timeout': self.timeout, 
        }
        if proxy is not None:
            params['proxies'] = { 'http': proxy, 'https': proxy }
            print ( 'using proxy: {}'.format(proxy))
            
        try:
            response = requests_retry_session(retries=self.retries).get(
                self.url, 
                **params
            )
#         except ProxyError as e:
#             print('Proxy Error: {}'.format( e.__class__.__name__))
#             print('retry without proxy ...')
#             self.connect()
        except requests.exceptions.RequestException as e:
            print('connection failed: {} {}'.format( 
                e.__class__.__name__, 
                self.url)
            )
            return e

        return response


    @lazy
    def res(self):
        if self.use_proxy:
            rs = self.connect(proxy=next(self.proxy_pool))
        else:    
            rs = self.connect()
        #return None if type(rs) is str else rs
        return rs
        

    @lazy
    def html(self):
        if isinstance(self.res, requests.models.Response) and \
                self.res.status_code == 200:
            return self.res.text

        return ''




    @lazy
    def sp(self):
        return BS(self.html, 'html5lib')

