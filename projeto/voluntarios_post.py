from sessao_pt import auth_token, api_url, headers
from Instruments import registros
import requests
import os




for registro in registros:
    dados_envio = {
        "iniciais": registro.get("demografia_iniciais",""),
    }

resposta_pt = requests.post(f"{api_url}/voluntarios", headers=headers, json=dados_envio)

if resposta_pt.status_code in (200, 201):
    print("Dados enviados com sucesso!")
else:
    print(f"Erro ao enviar dados: {resposta_pt.status_code} - {resposta_pt.text}")
    
    
    
    


