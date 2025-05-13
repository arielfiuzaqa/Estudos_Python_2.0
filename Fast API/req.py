import requests
from testeAPI import app

# Get
retorno = requests.get('http://127.0.0.1:8000/login')
print(retorno.json())
# Post
retorno = requests.post('http://127.0.0.1:8000/usuario', params={"id": 5, 'nome': 'Roberto', 'senha': '123456'})
print(retorno.json())