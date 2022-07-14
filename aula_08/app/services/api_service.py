import json
import requests
import ipdb

# from services import *
import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MyNewPass',
            database='aula_08'
        )
        print('Banco conectado!!')

        return conn

    except mysql.connector.Error as error:
        # return {"error in Mysql": error}
        print(error)



url = 'https://jsonplaceholder.typicode.com/users'


# ler os dados

# tratar os dados


response = requests.get(url)

content = []

for x in json.loads(response.content):
    x.pop('address')
    x.pop('company')
    content.append(x)


# content = []
# for x in json.loads(response.content):
#     tmp = {}
#     for y in x.items():
#        if y[0] != 'address' and y[0] != 'company':
#         tmp[y[0]] = y[1]
#     content.append(tmp)

# print(content)


def set_in_db(content):
    
    # conectar no banco
    conn = connect_db()

    # cursor
    cur = conn.cursor()

    for line in content:
        # query
        query = f"INSERT INTO users (name, username, email, phone, website) VALUES ({line['name']}, )"
        
        # executar a query
        cur.execute(query)

    # commit
    conn.commit()

    # fechar
    conn.close()

    return 'Dados gravados com sucesso!'


def get_all_in_db():
    
    # CONECTAR NO BANCO
    conn = connect_db()

    # DEFINIR O CURSOR
    cur = conn.cursor()

    # QUERY
    query = 'SELECT * FROM users'

    # EXECUTAR
    cur.execute(query)

    resultado = cur.fetchall()

    content = []

    for linha in resultado:
        content.append(linha)

    conn.close()

    print(content)

    
