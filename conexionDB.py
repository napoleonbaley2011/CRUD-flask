import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd = "",
        database = "tabla_carros"
    )
    if mydb:
        print ("Conexion exitosa")
        return mydb
    else:
        print("Error en la conexion") 