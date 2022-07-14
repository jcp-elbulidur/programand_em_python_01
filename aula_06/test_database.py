import mysql.connector

try:
    # conexao
    conn = mysql.connector.connect(
        host="localhost",
        user='root',
        password='p@ssword',
        database='aula_06'
    )
    print('opa deu bom')
except mysql.connector.error as error:
    print(error)


