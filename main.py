# coding=utf-8
import urllib
import json
import numpy as np
import re

url = "https://www.instagram.com/vintage.cybernetic/?__a=1"
parsed = json.load(urllib.urlopen(url))
nodes = parsed['graphql']['user']['edge_owner_to_timeline_media']['edges']
picArr = np.array([])

for key in nodes:
    if 'SOLD' in key['node']['edge_media_to_caption']['edges'][0]['node']['text']:
        text = 'SOLD'
    else:
        text = re.findall('dm to buy<3\\n\\n(.*)\\n-', key['node']['edge_media_to_caption']['edges'][0]['node']['text'])


    picArr = np.append(picArr, [key['node']['display_url'], key['node']['edge_liked_by']['count'], text])

with np.printoptions(precision=3, suppress=True):
    print(picArr)


#post: bild, likes, sold oder nicht
#statistik: wie viele artikel sold sind oder nicht
#welcher post hat die meisten likes
#welcher hat die wenigsten likes


