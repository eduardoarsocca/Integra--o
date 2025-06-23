# Importando bibliotecas
import requests
import dotenv
import os
import json
from urllib.parse import urljoin

# Carregando as variáveis do arquivo .env
dotenv.load_dotenv(override=True)
api_username = os.getenv('API_USERNAME')
api_password = os.getenv('API_PASSWORD')
api_url = os.getenv('API_URL')

# Iniciando a sessão
# Corpo do login a ser utilizado no acesso
body = {
    "nome": api_username,
    "password":api_password
}

# Obtençao do token de acesso à polotrial
auth_url = urljoin(api_url, "/sessions")

response = requests.post(auth_url, json = body)

# # Verificar a resposta
# print(f"Status Code: {response.status_code}")
# print(f"Headers: {response.headers}")
# print(f"Content: {response.text}")

# Extraindo o token
token = response.json()["token"]

# Incorporando a string Bearer para inserir
if token:
    auth_token = "Bearer " + token
    
else:
    print("Falha ao obter o token.")
    
headers = {"Authorization": auth_token}