import requests
from dataclasses import dataclass
import json
from selectolax.parser import HTMLParser
import re

@dataclass
class FlightData:
    price: float
    airline: str

@dataclass
class FlightScraper:

    # def get_header(self):
    #     base_url = 'https://oldmatrix.itasoftware.com'
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    #     }
    #     with requests.Session() as session:
    #         response = session.get(base_url, headers=headers)
    #     tree = HTMLParser(response.text)
    #     gwt = tree.css_first('script')
    #     return re.findall('/(.*).cache', gwt.attributes['src'])[0]

    def get_data(self):
        base_url = 'https://oldmatrix.itasoftware.com'
        search_url = 'https://oldmatrix.itasoftware.com/search'
        s = requests.Session()
        r = s.get(base_url)
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

        data = {"method":"summarize","params":"{\"2\":[\"carrierStopMatrix\",\"currencyNotice\",\"durationSliderItinerary\",\"itineraryArrivalTimeRanges\",\"itineraryCarrierList\",\"itineraryDepartureTimeRanges\",\"itineraryDestinations\",\"itineraryOrigins\",\"itineraryPriceSlider\",\"itineraryStopCountList\",\"solutionList\",\"warningsItinerary\"],\"3\":{\"4\":{\"1\":1,\"2\":2000},\"5\":{\"1\":1},\"7\":[{\"3\":[\"DPS\"],\"5\":[\"JKT\"],\"8\":\"2023-03-11\",\"9\":0,\"11\":1},{\"3\":[\"JKT\"],\"5\":[\"DPS\"],\"8\":\"2023-03-13\",\"9\":1,\"11\":0}],\"8\":\"COACH\",\"9\":1,\"10\":1,\"15\":\"SUNDAY\",\"16\":0,\"22\":\"default\",\"25\":1},\"4\":\"gmQ0dNkq5NAtmbb5TJBJ5Vvub\",\"5\":\"0CX8nVijEQI7Tszqm7seBU5\",\"6\":\"wholeTrip\"}"}
        r = s.post(search_url, json=data, headers=search_headers)
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