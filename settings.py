from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

SECRET_KEY_TOKEN_DR_CONSULTA = os.getenv("SECRET_KEY_TOKEN_EFETIVA_SAUDE")
CONNECTION_STRING_DB = os.getenv("CONNECTIONDB")
API_TOKEN_IUGU = os.getenv("API_TOKEN_IUGU")
RECIPIENT_ACCOUNT_ID= os.getenv("RECIPIENT_ACCOUNT_ID")
URL_API_IUGU_CUSTOMERS=os.getenv("URL_API_IUGU_CUSTOMERS")
URL_API_PAGAMENTO=os.getenv("URL_API_PAGAMENTO")
URL_CRIAR_SUB_CONTA=os.getenv("URL_CRIAR_SUB_CONTA")
URL_ENVIA_CONTA_VERIFICACAO=os.getenv("URL_ENVIA_CONTA_VERIFICACAO")
TOK_BOX_API_KEY=os.getenv("TOK_BOX_API_KEY")
API_SECRET_TOK_BOX=os.getenv("API_SECRET_TOK_BOX")