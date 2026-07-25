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

# Funcao de READ "R" do CRUD

def listar_permits():
    conexao = conectar()
    cursor = conexao.cursor()

    query = "SELECT * FROM permits"
    cursor.execute(query)

    resultados = cursor.fetchall()

    for permit in resultados:
        id, permit_number, address, parcel_id, permit_type, status, submitted_date, approval_date, expiration_date, inspector_notes = permit
        print(f"ID: {id}")
        print(f"Permit Number: {permit_number}")
        print(f"Endereço: {address}")
        print(f"Parcel ID: {parcel_id}")
        print(f"Tipo: {permit_type}")
        print(f"Status: {status}")
        print(f"Data de submissão: {submitted_date}")
        print(f"Data de aprovação: {approval_date}")
        print(f"Data de expiração: {expiration_date}")
        print(f"Notas: {inspector_notes}")
        print("-" * 30)

    cursor.close()
    conexao.close()


# Update "U" do CRUD

def atualizar_permit_number():
    id_permit = input("ID do permit que deseja atualizar: ")
    novo_permit_number = input("Novo Permit Number: ")

    conexao = conectar()
    cursor = conexao.cursor()

    query = """
        UPDATE permits
        SET permit_number = %s
        WHERE id = %s
    """
    valores = (novo_permit_number, id_permit)

    cursor.execute(query, valores)
    conexao.commit()

    if cursor.rowcount == 0:
        print("Esse ID não existe. Por favor, insira um ID válido.")
    else:
        print(f"Permit atualizado com sucesso!")

    cursor.close()
    conexao.close()


def cancelar_permit():
    id_permit = input("ID do permit que deseja cancelar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    query = """
        UPDATE permits
        SET status = 'cancelled'
        WHERE id = %s
    """
    valores = (id_permit,)

    cursor.execute(query, valores)
    conexao.commit()

    if cursor.rowcount == 0:
        print("Esse ID não existe. Por favor, insira um ID válido.")
    else:
        print("Permit cancelado com sucesso.")

    cursor.close()
    conexao.close()

# Roda a funcao: 

if __name__ == "__main__":
    cancelar_permit()