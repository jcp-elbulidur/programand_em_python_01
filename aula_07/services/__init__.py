import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MyNewPass',
            database='aula_07'
        )
        print('Banco conectado!!')

        return conn

    except mysql.connector.Error as error:
        # return {"error in Mysql": error}
        print(error)


        


