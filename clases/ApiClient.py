import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint, params=None):
        response = requests.get(f'{self.base_url}/{endpoint}', params=params)
        response.raise_for_status()
        return response.json()

    def post_data(self, endpoint, data):
        response = requests.post(f'{self.base_url}/{endpoint}', json=data)
        response.raise_for_status()
        return response.json()
