import mysql.connector
from dotenv import load_dotenv
import os
from datetime import date
from mysql.connector import IntegrityError

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

    if not resultados:
        print("Não há nenhum permit cadastrado no sistema.")
    else:
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

def atualizar_permit():
    id_permit = input("ID do permit que deseja atualizar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT status FROM permits WHERE id = %s", (id_permit,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Esse ID não existe. Por favor, insira um ID válido.")
        cursor.close()
        conexao.close()
        return

    status_atual = resultado[0]

    if status_atual == "cancelled":
        print("Esse permit já foi cancelado e não pode ser atualizado.")
        cursor.close()
        conexao.close()
        return

    print("\nO que deseja atualizar?")
    print("1 - Permit Number")
    print("2 - Aprovar permit (define data de aprovação como hoje)")
    print("3 - Data de expiração")
    print("4 - Notas do inspetor")

    opcao = input("Escolha uma opção: ")

    campos = {
        "1": "permit_number",
        "2": "approval_date",
        "3": "expiration_date",
        "4": "inspector_notes"
    }

    coluna = campos.get(opcao)

    if coluna is None:
        print("Opção inválida.")
        cursor.close()
        conexao.close()
        return

    if opcao == "2":
        novo_valor = date.today()
    elif opcao == "3":
        novo_valor = input("Nova data de expiração (AAAA-MM-DD): ")
    elif opcao == "4":
        novo_valor = input("Nova nota do inspetor: ")
    else:
        novo_valor = input("Novo Permit Number: ")

    query = f"UPDATE permits SET {coluna} = %s WHERE id = %s"
    valores = (novo_valor, id_permit)

    try:
        cursor.execute(query, valores)
        conexao.commit()
        print("Permit atualizado com sucesso!")

    except IntegrityError:
        print("Esse Permit Number já está em uso. Escolha um número diferente.")

    cursor.close()
    conexao.close()

# Delete "D" do CRUD

def cancelar_permit():
    id_permit = input("ID do permit que deseja cancelar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT status FROM permits WHERE id = %s", (id_permit,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Esse ID não existe. Por favor, insira um ID válido.")
        cursor.close()
        conexao.close()
        return

    status_atual = resultado[0]

    if status_atual == "cancelled":
        print("Esse permit já foi cancelado anteriormente.")
        cursor.close()
        conexao.close()
        return

    query = """
        UPDATE permits
        SET status = 'cancelled'
        WHERE id = %s
    """
    valores = (id_permit,)

    cursor.execute(query, valores)
    conexao.commit()

    print("Permit cancelado com sucesso.")

    cursor.close()
    conexao.close()

# Roda a funcao: 

if __name__ == "__main__":
    while True:
        print("\nO que deseja fazer agora?")
        print("1 - Cadastrar novo permit")
        print("2 - Visualizar permits cadastrados")
        print("3 - Atualizar permit")
        print("4 - Cancelar permit")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_permit()
        elif opcao == "2":
            listar_permits()
        elif opcao == "3":
            atualizar_permit()
        elif opcao == "4":
            cancelar_permit()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")