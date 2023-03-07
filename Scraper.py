import requests
from dataclasses import dataclass
import json
from pprint import pprint

@dataclass
class FlightScraper:
    def get_data(self, url, data, headers):
        with requests.Session() as session:
            response = session.post(url, json=data, headers=headers)
            return response.json()

if __name__ == '__main__':
    url = 'https://oldmatrix.itasoftware.com/search'
    data = {"method":"search","params":"{\"2\":[\"carrierStopMatrix\",\"currencyNotice\",\"durationSliderItinerary\",\"itineraryArrivalTimeRanges\",\"itineraryCarrierList\",\"itineraryDepartureTimeRanges\",\"itineraryDestinations\",\"itineraryOrigins\",\"itineraryPriceSlider\",\"itineraryStopCountList\",\"solutionList\",\"warningsItinerary\"],\"3\":{\"4\":{\"1\":1,\"2\":30},\"5\":{\"1\":1},\"7\":[{\"3\":[\"PAR\"],\"5\":[\"LON\"],\"8\":\"2023-03-11\",\"9\":1,\"11\":1},{\"3\":[\"LON\"],\"5\":[\"PAR\"],\"8\":\"2023-03-13\",\"9\":1,\"11\":1}],\"8\":\"COACH\",\"9\":1,\"10\":1,\"15\":\"SUNDAY\",\"16\":0,\"22\":\"default\",\"25\":1},\"4\":\"specificDates\",\"7\":\"!kpGlkczNAAZKh9k7aodCnvPxKh_hakQ7ADkAQSe-oaoMbQx_kT9usjF53Nt8auqy3kGYSzIbhTm8slVIsKusIwirhDTXMaOyv6B60L6tbGIJeDkCAAAAmFIAAAAqaAEHCgBaHDiqeCGZi-T4mXdjSmn8njR3XDeFbuCjFCSPCna8pTsE1uvHxFKpqqqW4VzITK4a1EmDUtcFsiYGsFoYy8ioFNAjlPrMR7N3F--g1KBPuveKdUpHjoJrHMDrmQLpSUB88EBwnCiXTSKK1arN-umTwK7OnuyD6wNJTMpgumRyoR-2QVpkOkMF3eXBhUV--4SuQiHsWoz_E-t8PohHNf2wGW6C9BknzlfW1XKcShAlT_KW7B0oWeoRo1LjG9YNxkpzXKdTYTYA74Nvsk8999HqsnwA_F1Fnb_cZUcerBYDjIi-E6BYTOfxuuOxM0d1-5R0KXVob3WX5D7LmWcnLUSSF1tkIBJWWu--CozgdVCRtnMUw4jEAywC4kdjrLVmFSDcZzkezltmtWTBSwlVXVOUT1rJlszydSSzxv5lx7QE77YLBeZLf5AKp7Vk79etEuNNyYg4-CVklQ4hJYIrhcNHwXYxVsEIyY4tdJcAtIeeYUrHKpoiRhLU6-tZZ3s0wZ-wi8CpG1skEu1zeIhkLGgzszBzSydNPCOWFgTrcC6pnSdj7kkQW0rjINH7YXGKTpMWpyi6cYfCIGzL-7SerXFyDMV0bl9AH_VPygXtTgyx2wv3HfS6I2E0iyfHb6YaA1DiOWh4JoqXlcjzkdsLpC8mHelY0gJth84MHYOiYz7b6RbCqbVx1lMlNKjjwC3Yp1330lfsx-rNG61GIZFAwgbTMWcrYD100lOnYOkqi7My9fUOBc2Olufx5bV8Y3JR5SKhpJxWUlxqYL5MHAhGROjMu0aMf1aQITignTB_KoNjtD0_c0z5a505zNBuczC7KeBZGgnflykKk15mAG4Yqsqdu4HN__PtMUqZkvWKMHeIesT_7ngPDELccmJ2Vn2FhZwiDdlv7fs3kIF3kHVGY0sc6gLJdp00TKCser5mf-lZWnl59WOjEGVKmxKyaFYGh6HeaYuXKBxgv6FwbBqx-Ukm8ZiYQv6r9uqiLu1djZzwB3_zKhTuasaW0_WXT2saYAXAqFDqvV-S33ks7r-wdQxgprfQVOal3f1s6rhEQ5yQXnyFNbHwf5v_kcyf7ndIXjFfZgocfSGQaDzoDZjLwFyHlXyd0GRTXw\",\"8\":\"wholeTrip\"}"}
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/javascript; charset=utf-8",
        "X-GWT-Permutation": "D09E53F8D02F5814C9611C2BAF2CE1C1",
        "X-GWT-Module-Base": "https://oldmatrix.itasoftware.com/gwt/",
        "Origin": "https://oldmatrix.itasoftware.com",
        "Alt-Used": "oldmatrix.itasoftware.com",
        "Connection": "keep-alive",
        "Referer": "https://oldmatrix.itasoftware.com/",
        "Cookie": "__utma=257790165.1013719343.1678047814.1678135134.1678229965.3; __utmz=257790165.1678047814.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=257790165; __utmb=257790165.2.10.1678229965; __utmt=1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }
    scraper = FlightScraper()
    result = scraper.get_data(url, data=data, headers=headers)
    print(result)
