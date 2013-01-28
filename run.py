from lxml import objectify
import requests


data = objectify.fromstring(requests.get('http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=MD2682').content)

print '{data.temp_c}c/{data.temp_f}f'.format(data=data)
