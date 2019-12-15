from common import config
import requests
import bs4

class HomePage:
    def __init__(self, site_id):
        self.config = config()['news_sites'][site_id]
        self.url = config()['news_sites'][site_id]['url']
        self._queries = config()['news_sites'][site_id]['queries']
        self._html = None
        self.visit()

    def visit(self):
        home_page_requests = requests.get(self.url)
        home_page_requests.raise_for_status()
        self._html = bs4.BeautifulSoup(home_page_requests.text,'html.parser')

    @property
    def article_link(self):
        link_list = []
        for link in self._select(self._queries["home_page_articles_link"]):
            if(link and link.has_attr('href')):
                link_list.append(link)
        return set(link["href"] for link in link_list)


    def _select(self,query_string):
        return self._html.select(query_string)
