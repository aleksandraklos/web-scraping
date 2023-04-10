import pandas as pd
import kaufland
import geocode
import zabka
import aldi
import polomarket
import folium

k = kaufland.get_kaufland()
k['url']='https://upload.wikimedia.org/wikipedia/commons/d/d0/Kaufland_Logo.svg'

p = polomarket.get_polomarket()
p['url'] = 'https://gazetki-promocyjne.pl/wp-content/uploads/2020/04/polomarket-logo.svg'

z = zabka.get_zabka()
z['url']='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Zabka_logo_2020.svg/1200px-Zabka_logo_2020.svg.png'

a = aldi.get_aldi()
a['url']='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Aldi_Nord_201x_logo.svg/1200px-Aldi_Nord_201x_logo.svg.png'


df = pd.concat([k, p, a, z])
df['size']=df.apply(lambda x: (40,40) if x['source'] in ['Kaufland','Aldi'] else ((90,70)
                    if x['source'] in 'Polomarket' else (35,10)), axis=1)

m = folium.Map(location=[52.20882169791089, 21.00865285874372], tiles='cartodbpositron', zoom_start=16)

for index, row in df.iterrows():
        gg = folium.Marker(
                location=[row['lat'], row['lng']],
                popup=row['source'],
                icon=folium.features.CustomIcon(row['url'], icon_size=row['size'])
            ).add_to(m)
        gg.add_to(m)

m.save(outfile='map.html')

print('Scraping done! In the folder of this project you can find a html file with a map. Just open it and you should immediately see the map in your browser.')
