from sessao_pt import auth_token, api_url, headers
import pandas as pd
import requests
from config import config
import os
import json
import dotenv

# Carregando as variáveis do arquivo .env
dotenv.load_dotenv(override=True)

#Chamando a rota de interesse
voluntarios=api_url + "/voluntarios?nested=True"
request_voluntarios = requests.get(voluntarios, headers=headers).json()
dataframe_voluntarios = pd.DataFrame(request_voluntarios)
print(dataframe_voluntarios)

