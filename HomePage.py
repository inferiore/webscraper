from NewsPage import NewsPage


class HomePage(NewsPage):

    def __init__(self, site_id):
        super().__init__(site_id)

    @property
    def article_link(self):
        link_list = []
        for link in self._select(self._queries["home_page_articles_link"]):
            if (link and link.has_attr('href')):
                link_list.append(link)
        return set(link["href"] for link in link_list)
