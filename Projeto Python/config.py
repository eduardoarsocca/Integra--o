import dotenv
import os

#carregando as variáveis do arquivo env
dotenv.load_dotenv(override=True)
token = os.getenv('TOKEN_API_REDCAP')
url = os.getenv('URL_REDCAP')

config = dict(
    api_token =token,
    api_url = url
)
