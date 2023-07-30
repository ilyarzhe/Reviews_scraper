import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, source : str) -> None:
        self._source : str = source

    @property
    def source(self) -> str:
        return self._source
    
    @source.setter
    def source(self, source : str) -> None:
        self._source = source

    def get_data(self, url: str) -> str:
        try:
            response = requests.get(url)

            if response.status_code == 200:
                print("Successfully got the data")
                data : str = response.text
                return data
            else:
                print(f'Request failed with status code : {response.status_code}')
                return None
        except requests.exceptions.RequestException as e:
            print(f'Error occurred during the request: {e}')
            return None
    def make_pretty(self,data: str) -> None:
        try:
            soup = BeautifulSoup(data, 'html.parser')
            return soup.prettify()
        except Exception as e:
            print (f'Erorr occured during prettifying: {e}')
            return None
    



