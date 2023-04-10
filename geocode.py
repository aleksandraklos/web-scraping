import requests
import json

def geocode(querystring):
    global r
    url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?"
    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    #print(response)
    if len(response["candidates"]) > 0:
        r = {'lat': response["candidates"][0]["location"]["y"],
                  'lng': response["candidates"][0]["location"]["x"], 'score': response["candidates"][0]["score"],
                   'address': response["candidates"][0]["address"]}
    return json.dumps(r)
