import requests
import pandas as pd
import json 
def get_zabka():
    print('Looking for Żabka shops!')
    url = "https://www.zabka.pl/ajax/shop-clusters.json"

    payload = {}
    headers = {
      'authority': 'www.zabka.pl',
      'accept': 'application/json, text/plain, */*',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://www.zabka.pl/znajdz-sklep',
      'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
      'cookie': 'CookieConsent={stamp:%27bZEnQaD+8CNRf/xAWtfVYqQGf9V7nwmWuJofpgP9HmQuUnPvl0zfHg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1602846985327%2Cregion:%27pl%27}; _gcl_au=1.1.272368756.1602846986; _ga=GA1.2.191000163.1602846986; _fbp=fb.1.1602846985891.1416727766; _hjid=ac0783fe-db52-4df3-9828-8c7554fe1f98; sessionID=3433298892705.847; _gid=GA1.2.283421591.1603370381; _hjIncludedInSessionSample=1; _hjTLDTest=1; _hjAbsoluteSessionInProgress=0; _gat_UA-125043911-1=1'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    a = str(response.text)
    lista_sklepow = json.loads(a)
    lista_sklepow=pd.DataFrame(lista_sklepow)
    lista_sklepow['source']='Żabka'
    return lista_sklepow