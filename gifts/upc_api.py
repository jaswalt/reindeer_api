from urllib.parse import urlparse
import httplib2 as http
import json

class ProductInfo:

    
    @classmethod
    def fetch_product_info(cls):
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        ch = http.Http()
        # hard code a upc for now
        upc = '4002293401102'
        lookup = urlparse(f'https://api.upcitemdb.com/prod/trial/lookup?upc={upc}')
        resp, content = ch.request(lookup.geturl(), 'GET', '', headers)
        data = json.loads(content)
        
        if resp.status == 200:
            cls.data = data

        
    @classmethod
    def display_product_info(cls):
        data = cls.data

        first_item = data.get('items')[0]
        name = first_item.get('title')
        sku = first_item.get('ean')
        description = first_item.get('description')
        image = first_item.get('images')[0]
        first_offer = first_item.get('offers')[0]
        price = first_offer.get('price')

        return name, sku, price, description, image