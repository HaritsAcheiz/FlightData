import requests
from dataclasses import dataclass
import json
from pprint import pprint

@dataclass
class FlightData:
    price: float
    airline: str

@dataclass
class FlightScraper:

    def get_data(self, url, data, headers):
        with requests.Session() as session:
            response = session.post(url, json=data, headers=headers)
            return response.json()

    def json_to_file(self, data, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(json.loads(data), indent=2))

if __name__ == '__main__':
    url = 'https://oldmatrix.itasoftware.com/search'
    data = {"method":"summarize","params":"{\"2\":[\"carrierStopMatrix\",\"currencyNotice\",\"durationSliderItinerary\",\"itineraryArrivalTimeRanges\",\"itineraryCarrierList\",\"itineraryDepartureTimeRanges\",\"itineraryDestinations\",\"itineraryOrigins\",\"itineraryPriceSlider\",\"itineraryStopCountList\",\"solutionList\",\"warningsItinerary\"],\"3\":{\"4\":{\"1\":1,\"2\":2000},\"5\":{\"1\":1},\"7\":[{\"3\":[\"PAR\"],\"5\":[\"LON\"],\"8\":\"2023-03-11\",\"9\":1,\"11\":1},{\"3\":[\"LON\"],\"5\":[\"PAR\"],\"8\":\"2023-03-13\",\"9\":1,\"11\":1}],\"8\":\"COACH\",\"9\":1,\"10\":1,\"15\":\"SUNDAY\",\"16\":0,\"22\":\"default\",\"25\":1},\"4\":\"4su0dNFHWiBSwo0bdWT2S537b\",\"5\":\"00OviYYvFDKPVXDaR7FAvj6\",\"6\":\"wholeTrip\"}"}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
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

    scraper = FlightScraper()
    result = scraper.get_data(url, data=data, headers=headers)
    result = json.dumps(result['result']['38'], indent=2)
    scraper.json_to_file(result, 'Lon-Par ticket.json')
    with open('Lon-Par ticket.json', 'r') as f:
        print(json.load(f))