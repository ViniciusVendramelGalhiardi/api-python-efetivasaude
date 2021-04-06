from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

#ENV EFETIVA_SAUDE
SECRET_KEY_TOKEN_DR_CONSULTA = os.getenv("SECRET_KEY_TOKEN_EFETIVA_SAUDE")

#CONN 
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=sql-server-db-efetiva-efetivasaude.database.windows.net;DATABASE=dbefetivasaude;UID=db_user;PWD=Templarios3@')
CONNECTION_STRING_DB = os.getenv("CONNECTIONDB")