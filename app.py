from flask import Flask , render_template, request, redirect, url_for, jsonify
from controller.controllerCarro import *

import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
aplicacion = app 
msg  =''
tipo =''

#INICIO
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/layout.html', miData = listaCarros())

#RUTAS

@app.route('/registrar-carro', methods=['GET','POST'])
def addCarro():
    return render_template('public/acciones/add.html')

#REGISTRO DE CARRO

@app.route('/carro', methods=['POST'])
def formAddCarro():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        year = request.form['year']
        color = request.form['color']
        puertas = request.form['puertas']
        favorito = request.form['favorito']

        if(request.files['foto'] != ''):
            file = request.files['foto']
            nombreArchivo = recibeFoto(file)
            resultadoData = registrarCarro(marca, modelo, year, color, puertas, favorito, nombreArchivo)
            if(resultadoData ==1):
                return render_template('public/layout.html', miData = listaCarros(), msg='El registro fue exitoso', tipo=1)
            else:
                return render_template('public/layout.html', msg='Metodo HTTP incorrecto', tipo=1)
        else:
            return render_template('public/layout.html', msg = 'Debe cargar una foto', tipo=1)


def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static/assets/fotos_carros', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

@app.route('/ver-detalles-del-carro/<int:idCarro>',methods=['GET', 'POST'])
def viewDetalleCarro(idCarro):
    msg = ''
    if request.method == 'GET':
        resultadoData = detallesdelCarro(idCarro)

        if resultadoData:
            return render_template('public/acciones/view.html', infoCarro=resultadoData, msg= 'Detalle del Carro', tipo=1)
        else:
            return render_template('public/layout.html', msg = 'No existe el carro', tipo=1)
    
    return redirect(url_for('inicio'))




if __name__ == "__main__":
    app.run(debug=True, port=5000)