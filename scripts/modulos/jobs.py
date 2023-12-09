import requests
from lxml import html

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'

data=requests.get(url)
dataJSON=data.json()
print(data.json())
