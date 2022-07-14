from flask import Flask, request
from services import connect_db

app = Flask(__name__)

@app.route('/')
def home():
    conn = connect_db()
    
    cursor = conn.cursor()

    query = 'Show tables'
    cursor.execute(query)

    tables = cursor.fetchall()

    for x in tables:
        print(x)

    return 'Ola todos!!!'

@app.route('/mysql', methods=['POST'])
def set_data():

    data = request.get_json()

    # conectar no banco
    conn = connect_db()

    # cursor
    cur = conn.cursor()

    # criar queries
    query = f"INSERT INTO users (name, email, password) VALUES ({data['name'], {data['email'], {data['password']}}})"

    # Executar as queries
    cur.execute(query)

    # commitar as queries
    conn.commit()

    # Fechar conexao
    conn.close()

    return 'Dados gravados com sucesso!'

@app.route('/mysql')
def get_data():
    
    # conexao
    conn = connect_db()

    # criar o cursor
    cur = conn.cursor()
    # criar a query
    query = f'SELECT * FROM use'

    # Exxecutar minha query
    cur.execute(query)

    result = cur.fetchall()

    conn.close()

    return {"results": result}

    return ''


@app.route('/mysql/<id>', methods=['PATCH'])
def update_data(id):

    data = request.get_json()
    
    # conn
    conn = connect_db()

    # cria cursor
    cur = conn.cursor()

    # query
    query = f"UPDATE users SET nome = {data} WHERE id = {id}"

    # executar query
    cur.execute(query)

    # permanecer no banco
    conn.commit()

    # fechar conexao
    conn.close()

    return ''


@app.route('/test/<id>', methods=['PATCH'])
def test(id):
    return {"return": id}



