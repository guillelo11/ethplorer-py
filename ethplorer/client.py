import requests


class Client:
    API_URL = 'https://api.ethplorer.io'
    API_KEY = {"apiKey": "freekey"}

    def __init__(self, url=''):
        self.http_client = requests.session()

    def connect(self):
        try:
            response = self.http_client.get(self.url, params=self.API_KEY)
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.ConnectionError:
            print('Connection error')

    def build_url(self, endpoint, path = ''):
        self.url = self.API_URL + endpoint + path
