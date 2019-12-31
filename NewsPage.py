from common import config
import requests
import bs4


class NewsPage:

    def __init__(self, site_id,link=None):
        self.config = config()['news_sites'][site_id]
        self.url = link if link else config()['news_sites'][site_id]['url']
        self._queries = config()['news_sites'][site_id]['queries']
        self._html = None
        self.visit()

    def visit(self):
        home_page_requests = requests.get(self.url)
        home_page_requests.raise_for_status()
        self._html = bs4.BeautifulSoup(home_page_requests.text,'html.parser')

    def _select(self,query_string):
        return self._html.select(query_string)
