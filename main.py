import mysql.connector
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()

# Conectado o banco de dados:

def conectar():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conexao

# Criando funcao de cadastrar permit - "C" DO CRUD

def cadastrar_permit():
    address = input("Endereco: ")
    parcel_id = input("Parcel ID: ")
    permit_type = input("Tipo de permit (building, demolition): ")
    submitted_date = date.today()

    conexao = conectar()
    cursor = conexao.cursor()

    query = """
        INSERT INTO permits (address, parcel_id, permit_type, submitted_date)
        VALUES (%s, %s, %s, %s)
    """
    valores = (address, parcel_id, permit_type, submitted_date)

    cursor.execute(query, valores)
    conexao.commit()

    print(f"Permit cadastrado com sucesso! ID: {cursor.lastrowid}")

    cursor.close()
    conexao.close()

def listar_permits():
    conexao = conectar()
    cursor = conexao.cursor()

    query = "SELECT * FROM permits"
    cursor.execute(query)

    resultados = cursor.fetchall()

    for permit in resultados:
        print(permit)

    cursor.close()
    conexao.close()


if __name__ == "__main__":
    listar_permits()