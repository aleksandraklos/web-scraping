import requests
import json
import pandas as pd
def get_kaufland():
    print('Looking for Kaufland shops!')
    
    url = "https://www.kaufland.pl/.klstorefinder.json"

    payload={}
    headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
      'X-Requested-With': 'XMLHttpRequest',
      'Connection': 'keep-alive',
      'Referer': 'https://www.kaufland.pl/dla-klienta/sklepy.html',
      'Cookie': 'storeName=PL1060; CookieConsent={stamp:%27bmIf/ljzMlkWCsw7yoi8SJ8k5X3idKtS5KIAVfypJdVH1Zhyv2EW6w==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1606378187671%2Cregion:%27pl%27}; _fbp=fb.1.1606378187872.1118313125; AMCV_BCF65C6655685E857F000101%40AdobeOrg=870038026%7CMCIDTS%7C18601%7CMCMID%7C00696306319229763984430669652853309332%7CMCAID%7CNONE%7CMCOPTOUT-1607090391s%7CNONE%7CMCAAMLH-1607687991%7C6%7CMCAAMB-1607687991%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18608%7CvVersion%7C5.0.0; s_ecid=MCMID%7C00696306319229763984430669652853309332; TS0194e86f=014c3ac9f071d9af3e4cb6e9fe696736b8a5e6b0ec1112c01c3faddf985a5720ce3db45caad9c9407d613d521c19dd50cb1e79683f; AMCVS_BCF65C6655685E857F000101%40AdobeOrg=1; s_dfa=kauflklplprod; _idtsab=1607083192263; gpv_Page=kl%3Apl%3Apl%3Adla-klienta%3Asklepy; gpv_featureType=Stores%7CStore%20Profile; s_ppv=kl%253Apl%253Apl%253Adla-klienta%253Asklepy%2C70%2C29%2C1683%2C2%2C3; s_ips=704; s_tp=2388; s_plt=1.08; s_pltp=kl%3Apl%3Apl%3Adla-klienta%3Asklepy; s_cc=true; s_sq=kauflklplprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dkl%25253Apl%25253Apl%25253Adla-klienta%25253Asklepy%2526link%253DZmie%2525C5%252584%252520sklep%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dkl%25253Apl%25253Apl%25253Adla-klienta%25253Asklepy%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.kaufland.pl%25252Fdla-klienta%25252Fsklepy.html%252523%2526ot%253DA; TS0194e86f=014c3ac9f071d9af3e4cb6e9fe696736b8a5e6b0ec1112c01c3faddf985a5720ce3db45caad9c9407d613d521c19dd50cb1e79683f'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    a = json.loads(response.text)
    lista_sklepow = []
    for element in a:
        sklep = {"id": element["n"],"name": element["cn"], "lat":element["lat"],"lng":element["lng"],"address":element["sn"] + " " + element["pc"] + " " + element["t"]}
        lista_sklepow.append(sklep)

    import pandas as pd
    lista_sklepow=pd.DataFrame(lista_sklepow)
    lista_sklepow['source']='Kaufland'
    return lista_sklepow