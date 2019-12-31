import argparse
from requests import HTTPError
from urllib3.exceptions import MaxRetryError
from common import config
import logging
import re
from HomePage import HomePage
import ArticlePage as News

logging.basicConfig(level=logging.INFO)
is_well_formed_link = re.compile(r'https?://.+/.+$')
is_root_path = re.compile(r'.+$')

def _news_scraper(key):
    host = config()["news_sites"][key]['url']
    logging.info(f'scrap to %s',(key))
    home_page = HomePage(key)
    articles = []
    for link in home_page.article_link:
        article = _fetch_article(key,host,link)
        if(article):
            logging.info("Article fetched!!")
            articles.append(article)
        print(_build_link(host, link))

def _fetch_article(key,host,link):
    logging.info('start to log article at:{}'.format(_build_link(host,link)))
    article = None
    try:
        article = News.ArticlePage(key=key,link=(_build_link(host,link)))
    except (HTTPError,MaxRetryError) as e:
        logging.warning("error while fetching article",exc_info=False)

    if article and not article.body:
        logging.warning("article invalid there is not body")
        return None
    return article
def _build_link(host,link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host,link)
    else:
        return '{}/{}'.format(host, link)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument("news_site",help="the new site that you want to scrape",type=str,choices=new_sites_choices)
    args = parser.parse_args()
    _news_scraper(args.news_site)
