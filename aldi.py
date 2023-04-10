import json
import requests
import pandas as pd
from lxml.html import fromstring
from geocode import geocode
from time import sleep

def get_aldi():

    print('Looking for Aldi shops! This one will take a bit longer... You will be provided with updates about the progress.')
    url = 'https://www.aldi.pl/informacje-dla-klienta/wyszukiwarka-sklepu.html'
    api_url = 'https://aldi.pl'
    r = requests.get(url)
    html = fromstring(r.text)
    links = html.cssselect('a')
    a = [l.attrib['href'] for l in links if 'wyszukiwarka-sklepu/' in l.attrib['href']]

    all_links = []
    all_links_details = []

    # linki do miast
    print('Iterating over 1st out of 4 loops.')
    for link in a:
        html = fromstring(requests.get(api_url + link).text)
        links2 = [l.attrib['href'] for l in html.cssselect('a') if 'wyszukiwarka-sklepu/' in l.attrib['href']]
        all_links.extend(links2)
    
    print('Iterating over 2nd out of 4 loops.')
    for link in all_links:
        html = fromstring(requests.get(api_url + link).text)
        links2 = [l.attrib['href'] for l in html.cssselect('div.mod-stores__overview a')]
        all_links_details.extend(links2)
    shops=[]
    
    print('Iterating over 3rd out of 4 loops.')
    for link in all_links_details:
        html = fromstring(requests.get(api_url + link).text)
        data = html.cssselect('div.mod-stores__detail')[0]
        item = {}
        item['name'] = data.cssselect('h5.mod-stores__detail-label')[0].text_content()
        item['chain'] = 'store_aldi'
        item['address'] = data.cssselect('span[itemprop="streetAddress"]')[0].text_content() + \
                          ', ' + data.cssselect('span[itemprop="addressLocality"]')[0].text_content()
        item['url'] = api_url + all_links_details[0]
        item['lat'] = 0
        item['lng'] = 0
        item['geocode'] = True

        data = html.cssselect('div.mod-stores__detail-col')[1]
        item['info'] = {}
        item['info']['hour'] = data.text_content().strip().replace('\t', '').replace('\n', '').replace('  ', '')
        data = html.cssselect('div.mod-stores__detail-col')[2]
        item['info']['details'] = data.text_content().strip().replace('\t', '').replace('\n', '').replace('  ', '')
        item['id'] = ''
        shops.append(item)
        
    df=pd.DataFrame(shops)
    df['lat']=""
    df['lng']=""
    df['resp']=""
    
    print('Iterating over 4th out of 4 loops.')
    for i in range(0, len(df)):
        querystring = {"Address": df['address'][i] ,  "outFields": "%2A",
                           "forStorage": "false", "f": "pjson", "countryCode": "PL"}
        try:
            response=json.loads(geocode(querystring))
            if 'error' not in response:
                df.at[i, 'lat']=response['lat']
                df.at[i, 'lng']=response['lng']
                df.at[i, 'resp']= response['address']
            else:
                continue
        except:
            pass
    df['source']='Aldi'
    return df