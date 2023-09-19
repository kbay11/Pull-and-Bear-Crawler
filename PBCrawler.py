import requests
import json
from fake_useragent import UserAgent


with open('info.json', "r") as json_file:
        data = json.load(json_file)

stores = data['stores']
languages = data['languages']


class Crawler:
    def __init__(self, store, language='EN',):
        self.store_name = store
        self.language_name = language
        self.language = languages[language]
        self.store = stores[store]
        self.agent = UserAgent()


    def get_product_details(self, product_ids, file_name=None, category_name=None):
        headers = {
            'user-agent': self.agent.random,
            }

        params = (
            ('productIds', ','.join([str(i) for i in product_ids])),
            ('languageId', self.language),
            ('appId', '1'),
            )
        
        response = requests.get(f'https://www.pullandbear.com/itxrest/3/catalog/store/{self.store[0]}/{self.store[1]}/productsArray', headers=headers, params=params)

        if not file_name:
            file_name = f'{self.store_name}_{self.language}_products.json'
        
        if category_name:
            file_name = f'{self.store_name.lower()}_{self.language_name.lower()}_{category_name}.json'
    
        with open(file_name, "w") as json_file:
            json.dump(response.json(), json_file)

    def get_all_products_from_category(self, category_id, category_name):
        headers = {
            'user-agent': self.agent.random,
            }

        params = (
            ('languageId', self.language),
            ('showProducts', 'false'),
            ('appId', '1'),
            )
        
        response = requests.get(f'https://www.pullandbear.com/itxrest/3/catalog/store/{self.store[0]}/{self.store[1]}/category/{category_id}/product', headers=headers, params=params)

        products = response.json()['sortedProductIds']

        self.get_product_details(products, category_name=category_name)

