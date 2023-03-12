import requests
from dataclasses import dataclass
import json
from selectolax.parser import HTMLParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@dataclass
class FlightData:
    price: float
    airline: str

@dataclass
class FlightScraper:

    def get_data(self):
        base_url = 'https://oldmatrix.itasoftware.com'
        search_url = 'https://oldmatrix.itasoftware.com/search'

        base_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Alt-Used': 'oldmatrix.itasoftware.com',
            'Connection': 'keep-alive',
            # 'Cookie': '__utma=257790165.484331316.1678481868.1678481868.1678487054.2; __utmc=257790165; __utmz=257790165.1678481868.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }

        s = requests.Session()
        r = s.get(base_url)
        ff_opt = Options()
        ff_opt.add_argument('-headless')
        driver = webdriver.Firefox(options=ff_opt)
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        searchkey = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,'input#searchKey-0'))).get_attribute('value')
        session_id = driver.session_id
        print(searchkey)
        print(session_id)
        driver.quit()
        search_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/javascript; charset=utf-8',
            'X-GWT-Permutation': 'D09E53F8D02F5814C9611C2BAF2CE1C1',
            'X-GWT-Module-Base': 'https://oldmatrix.itasoftware.com/gwt/',
            'Origin': 'https://oldmatrix.itasoftware.com',
            'Alt-Used': 'oldmatrix.itasoftware.com',
            'Connection': 'keep-alive',
            'Referer': 'https://oldmatrix.itasoftware.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        search_headers2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/javascript; charset=utf-8',
            'X-GWT-Permutation': 'D09E53F8D02F5814C9611C2BAF2CE1C1',
            'X-GWT-Module-Base': 'https://oldmatrix.itasoftware.com/gwt/',
            'Origin': 'https://oldmatrix.itasoftware.com',
            'Alt-Used': 'oldmatrix.itasoftware.com',
            'Connection': 'keep-alive',
            'Cookie': '__utma=257790165.193650672.1678572821.1678572821.1678572821.1; __utmb=257790165.1.10.1678572821; __utmc=257790165; __utmz=257790165.1678572821.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1',
            'Referer': 'https://oldmatrix.itasoftware.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        data2 = {"method":"summarize","params":"{\"2\":[\"carrierStopMatrix\",\"currencyNotice\",\"durationSliderItinerary\",\"itineraryArrivalTimeRanges\",\"itineraryCarrierList\",\"itineraryDepartureTimeRanges\",\"itineraryDestinations\",\"itineraryOrigins\",\"itineraryPriceSlider\",\"itineraryStopCountList\",\"solutionList\",\"warningsItinerary\"],\"3\":{\"4\":{\"1\":1,\"2\":2000},\"5\":{\"1\":1},\"7\":[{\"3\":[\"PAR\"],\"5\":[\"LON\"],\"8\":\"2023-03-11\",\"9\":1,\"11\":1},{\"3\":[\"LON\"],\"5\":[\"PAR\"],\"8\":\"2023-03-18\",\"9\":1,\"11\":1}],\"8\":\"COACH\",\"9\":1,\"10\":1,\"15\":\"SUNDAY\",\"16\":0,\"22\":\"default\",\"25\":1},\"4\":\"WLk0dNz2qg001oapG3d9Oo1Ih\",\"5\":\"0QueCqbg7OEAOueLE5GvKdI\",\"6\":\"wholeTrip\"}"}
        r = s.post(search_url, json=data2, headers=search_headers2)
        return r.json()

    def json_to_file(self, data, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(json.loads(data), indent=2))

if __name__ == '__main__':
    scraper = FlightScraper()
    result = scraper.get_data()
    print(result)
    # result = json.dumps(result['result']['38'], indent=2)
    # scraper.json_to_file(result, 'Lon-Par ticket.json')
    # with open('Lon-Par ticket.json', 'r') as f:
    #     print(json.load(f))