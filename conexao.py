import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="pdv"
    )
