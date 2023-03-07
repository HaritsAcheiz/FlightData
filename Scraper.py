import requests
# from requests_html import HTMLSession
from dataclasses import dataclass
from selectolax.parser import HTMLParser
import json
from bs4 import BeautifulSoup

@dataclass
class FlightScraper:
    def fetch(self):
        url = 'https://oldmatrix.itasoftware.com/'
        with requests.Session() as session:
            response = session.get(url)
            return response.text
    def parser(self, html):
        tree = HTMLParser(html)
        parent = tree.css_first('div#pageContentNode > div > div > div > div#contentwrapper')
        child = tree.css_first('div.gwt-TabPanelBottom > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')

        return data

if __name__ == '__main__':
    scraper = FlightScraper()