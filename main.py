import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conexao

if __name__ == "__main__":
    conexao = conectar()
    print("Conectado com sucesso!")
    conexao.close()