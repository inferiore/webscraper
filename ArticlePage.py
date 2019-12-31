from NewsPage import NewsPage


class ArticlePage (NewsPage):
    def __init__(self,key,link):
        super().__init__(key,link)

    @property
    def body(self):
        result = self._select(self._queries["article_body"])
        return result
    @property
    def title(self):
        result = self._select(self._queries["article_title"])
        return result
