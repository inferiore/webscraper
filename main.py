import argparse
from common import config
import logging
import HomePage

logging.basicConfig(level=logging.INFO)

def _news_scraper(key):
    host = config()["news_sites"][key]['url']
    logging.info(f'scrap to %s',(key))
    home_page =  HomePage.HomePage(key);

    print(home_page.article_link)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument("news_site",help="the new site that you want to scrape",type=str,choices=new_sites_choices)
    args = parser.parse_args()
    _news_scraper(args.news_site)

