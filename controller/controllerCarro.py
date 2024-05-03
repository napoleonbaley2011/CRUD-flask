from random import sample
from conexionDB import *

def listaCarros():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM carros ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda

def registrarCarro(marca='', modelo='', year='', color='', puertas='', favorito='', nombreArchivo=''):
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cursor           = conexion_MySQLdb.cursor(dictionary=True)

    consulta = ("INSERT INTO carros(marca, modelo, year, color, puertas, favorito, foto) Values (%s, %s, %s, %s, %s, %s, %s)")
    valores = (marca, modelo, year, color, puertas, favorito, nombreArchivo )
    cursor.execute(consulta,valores)

    conexion_MySQLdb.commit()
    cursor.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD

    resultado_insert = cursor.rowcount
    ultimo_id = cursor.lastrowid
    return resultado_insert 

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio



def detallesdelCarro(idCarro):
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cursor           = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM carros WHERE id = '%s'" % (idCarro,))
    resultado = cursor.fetchone()
    cursor.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD

    return resultado