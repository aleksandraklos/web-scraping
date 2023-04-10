import requests
import json
from lxml.html import fromstring
from requests_html import HTMLSession
import pandas as pd

def get_polomarket():
    print('Looking for Polomarket shops!')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    data = requests.get('https://www.polomarket.pl/?xml=module&module_type=google_map_preload&gmr=12&gmc=', headers=headers).json()

    opcje = fromstring(data['filters'])
    values = [o.attrib['value'] for o in opcje.cssselect('option') if len(o.attrib['value']) == 2]

    df1 = pd.DataFrame(columns=['source','lat','lng','id','name','address'])
    i = 0
    for v in values:
        data = requests.get('https://www.polomarket.pl/?xml=module&module_type=google_map_preload&gmr={}&gmc='.format(v), headers=headers).json()
        stores = fromstring(data['regions'])
        cities = stores.cssselect('div.col-md-2.js-data')
        streets = stores.cssselect('div.col-md-3.js-data')
        hours = stores.cssselect('div.col-md-5.js-data.open')
        latlng = stores.cssselect('a')#[0].attrib['data-lat']
        for c, s, ll, h in zip(cities,streets,latlng,hours):
            i = i + 1 
            df1.at[i, "address"] = s.text_content().replace('Ulica:','').strip() + ', ' + c.text_content().replace('Miasto:','').strip()
            df1.at[i, "source"] = 'Polomarket'
            df1.at[i, 'lat'] = float(ll.attrib['data-lat'])
            df1.at[i, 'lng'] = float(ll.attrib['data-lng'])
    return df1
