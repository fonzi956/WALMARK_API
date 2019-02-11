import requests
import json

url_api = '_api_url'

json_data = requests.get(url_api).json()
#print(json_data)

items_count = len(json_data['items'])
items = json_data['items']

for item in range(items_count):
    print ("{i}: ${p}".format(i=items[item]['name'], p=items[item]['salePrice']))
    print ()



#print(items)