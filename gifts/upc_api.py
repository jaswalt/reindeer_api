from urllib.parse import urlparse
import json
import httplib2 as http
from django.utils.html import strip_tags
import html.parser
html_parser = html.parser.HTMLParser()

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
        resp, content = ch.request(
            f'https://api.upcitemdb.com/prod/trial/lookup?upc={upc}', 
            'GET',
            None,
            headers
        )
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
                resp, content = ch.request(
                    f'http://api.walmartlabs.com/v1/items?apiKey={api_key}&upc={walmart_upc}',
                    'GET',
                    None,
                    headers
                )
                walmart_data = json.loads(content)
                walmart_item = walmart_data.get('items')[0]
                name = walmart_item.get('name')
                sku = walmart_item.get('upc')
                price = walmart_item.get('salePrice')
                description_with_tags = walmart_item.get('shortDescription')
                unescaped = html.parser.unescape(description_with_tags)
                description = strip_tags(unescaped)
                image = walmart_item.get('largeImage')

                return name, sku, price, description, image              

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

ProductInfo.fetch_product_info()