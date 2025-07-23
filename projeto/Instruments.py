#!/usr/bin/env python

from config import config
import requests
import json
import pandas as pd
from urllib.parse import urljoin
from sessao_pt import auth_token, api_url, headers

#Requisição para o conteúdo do projeto de integração
## Conteúdo extraído
payload = {
    'token': config['api_token'],
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat', # 'eav' para exportar como formato de valor-atributo ou 'flat' para exportar como formato plano
    'csvDelimiter': '',
    'fields[0]': 'record_id',
<<<<<<< HEAD
    'fields[1]': 'demografia_iniciais',
=======
    'fields[2]': 'demografia_iniciais',
>>>>>>> 17096cca4c25b415d0bdee61bcee4b6d5386f778
    'returnFormat': 'json'
}

#Verificando a conexão com o servidor e extraindo os campos desejados
print('Conectando ao servidor...')
resposta = requests.post(config['api_url'],data=payload) #mudei de post para get
resposta.raise_for_status()  # Verifica se a requisição foi bem sucedida




if resposta.status_code == 200:
    print('Conexão bem sucedida!')
    registros = resposta.json()
    # Lendo o json com o pandas
    data = pd.DataFrame(registros)
    print('Campos extraídos com sucesso!')
    print(data.head(6))  # Exibe as primeiras linhas do DataFrame
    print(f"Extraídos {len(registros)} registros do REDCap.")
