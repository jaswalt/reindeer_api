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
        upc = '062020005632' #'4002293401102'
        lookup = urlparse(f'https://api.upcitemdb.com/prod/trial/lookup?upc={upc}')
        resp, content = ch.request(lookup.geturl(), 'GET', '', headers)
        data = json.loads(content)

        if data['code'] == 'OK':
            cls.data = data
            item_length = len(data.get('items'))
            if item_length > 0:
                # below line isn't working, find a way to call below method
                cls.display_product_info()
            else:
                #search another api
                walmart_upc = '035000521019'
                api_key = '4n29ferqah8jjbatzb7v2vgw'
                walmart_lookup = urlparse(f'http://api.walmartlabs.com/v1/items?apiKey={api_key}&upc={walmart_upc}')
                resp, content = ch.request(walmart_lookup.geturl(), 'GET', headers)
                walmart_data = json.loads(content)
                print(walmart_data)      
            
        elif data['code'] == 'INVALID_UPC':
            # tell client to manually enter info
            cls.data = {'code': 'not found'}     


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

