from urllib.parse import urlparse
import httplib2 as http
import json


def fetch_product_info():
    
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
        return data
    else:
        return None


def product_info(data):
    if data is None:
        return data

    first_item = data.get('items')[0]
    name = first_item.get('title')
    sku = first_item.get('ean')
    first_offer = first_item.get('offers')[0]
    price = first_offer.get('price')
    

    return name, sku, price