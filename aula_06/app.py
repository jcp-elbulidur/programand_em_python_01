from flask import Flask, request
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem vindo ao flask'


@app.route('/enviar', methods=['POST'])
def mostrar_dados():
    dados = request.get_json()

    return {"resultado": dados}

data = []


# Criando um CSV
@app.route('/csv', methods=['POST'])
def set_csv():
    payload = request.get_json()

    fieldnames = [x for x in payload.keys()]

    file = open("filmes.csv", "a") # Append

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # writer.writerow({"id": "id", "filme":"filme", "lancamento": "lancamento", "nota":"nota"})
    writer.writerow(payload)

    file.close()

    return {"message": "Dados gravado com sucesso!"}


# 

#Lendo csv
@app.route('/csv', methods=['GET'])
def get_csv():
    
    file = open('filmes.csv', 'r')

    reader = csv.DictReader(file)

    data = []

    for line in reader:
        data.append(line)

    return {"results": data}


# aDCIONA MAIS DE UMA LINHA NO CSV
# ROTA PARA LER O FILME COM ID 2


@app.route('/csv_id_2', methods=['GET'])
def get_csv():

    file = open('filmes.csv', 'r')

    reader = csv.DictReader(file)

    data = []

    for line in reader:
        data.append(line)

    return {"results": data[1]}

# CODIGO ===> MYSQL ==> INFORMACOES
# INSTALLL LIB ===> MYSQL ===> SQL

# LIB ==> SQL


























