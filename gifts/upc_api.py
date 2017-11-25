import json
import os
import html.parser
import httplib2 as http
from django.utils.html import strip_tags
html_parser = html.parser.HTMLParser()

class ProductInfo:

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    ch = http.Http()

    @classmethod
    def fetch_upc_info(cls):
        # hard code a upc for now
        upc =  '062020005632'#--valid upc but no items-- #'4002293401102' #--valid upc with many items--
        resp, content = cls.ch.request(
            f'https://api.upcitemdb.com/prod/trial/lookup?upc={upc}', 
            'GET',
            None,
            cls.headers
        )
        data = json.loads(content)

        if data['code'] == 'OK':

            cls.data = data
            item_length = len(data.get('items'))

            if item_length > 0:
                
                first_item = data.get('items')[0]
                name = first_item.get('title')
                sku = first_item.get('ean')
                description = first_item.get('description')
                image = first_item.get('images')[0]
                first_offer = first_item.get('offers')[0]
                price = first_offer.get('price')

                return name, sku, price, description, image

            else:
                #search another api
                walmart_upc = '035000521019'
                resp, content = cls.ch.request( 
                    f"http://api.walmartlabs.com/v1/items?apiKey={os.environ.get('WALMART_API_KEY')}&upc={walmart_upc}",
                    'GET',
                    None,
                    cls.headers
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
            cls.data = {'code': 'sku not found'}


    @classmethod
    def fetch_search_info(cls):
        # hard code a product search for now
        product = 'bycicle' #--returns 5 items--  #'books' #--code: not found-- 
        resp, content = cls.ch.request(
            f'https://api.upcitemdb.com/prod/trial/search?s={product}',
            'GET',
            None,
            cls.headers
        )
        data = json.loads(content)

        if data['code'] == 'OK':
            cls.data = data
            items = data.get('items')
            names = [li['title'] for li in items]
            images_array = [li['images'] for li in items]
            images = []
            for li in images_array:
                try:
                    images.append(li[0])
                except IndexError:
                    images.append('No image available')

            offers_array = [li['offers'] for li in items]
            first_offers = []
            for li in offers_array:
                try:
                    first_offers.append(li[0])
                except IndexError:
                    first_offers.append({'price': 'Price not available.'})
            prices = [li['price'] for li in first_offers]
            descriptions = []
            for li in items:
                if li['description'] == '':
                    descriptions.append('No description available.')
                else:
                    descriptions.append(li['description'])

            return names, prices, images, descriptions

        else:
            #search walmart api
            walmart_product = 'books'
            resp, content = cls.ch.request(
                f"http://api.walmartlabs.com/v1/search?apiKey={os.environ.get('WALMART_API_KEY')}&query={walmart_product}",
                'GET',
                None,
                cls.headers
            )
            walmart_data = json.loads(content)
            walmart_items = walmart_data.get('items')

            names = [li['name'] for li in walmart_items]
            prices = [li['salePrice'] for li in walmart_items]
            images = [li['largeImage'] for li in walmart_items]
            # escaping tags is not working
            default_descriptions = 'None'
            descriptions_with_tags = [li.get('shortDescription', default_descriptions) for li in walmart_items]
            #unescaped = html.parser.unescape(descriptions_with_tags)
            #descriptions = strip_tags(unescaped)

            return names, prices, images, descriptions_with_tags

#TO-DO: -Strip description tags in walmart search.
#       -Make sure descriptions work in first search (exceeded daily limit on nov.25)
#       -Receive barcode from react native