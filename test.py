import requests

url = 'localhost:5000/serverlogs/api/v0.1/testes'
response = requests.get(url, auth=('Antonio', 'v2com'))
response.json
response.text
