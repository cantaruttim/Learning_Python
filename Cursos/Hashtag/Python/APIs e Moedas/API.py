import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/last/:moedas')
print(cotacoes)