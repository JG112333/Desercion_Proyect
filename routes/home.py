from flask import Blueprint, redirect, render_template, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')

# Ruta para el formulario
@home_bp.route('/formulario')
def formulario():
    return render_template('formulario.html')  # Esto renderiza formulario.html



# Nueva ruta en home.py para redirigir a la ruta traerS3r
@home_bp.route('/ultimas_predicciones')
def ultimas_predicciones():
    return redirect(url_for('traerS3_lista.traers3r')) 

# Nueva ruta en home.py para redirigir a la ruta traerS3r
@home_bp.route('/chatbot_pagina')
def chatbot_pagina():
    return redirect(url_for('chatbot_handler.chatbot_page')) 

# Ruta para cargar y transformar el archivo
@home_bp.route('/transformar_cargar')
def transformar_cargar():
    return render_template('transformarDatos.html', archivo_generado=False)

# Ruta para cargar y transformar el archivo
@home_bp.route('/cargar_datos')
def cargar_datos():
    return render_template('cargarDatos.html', archivo_generado=False)

# Ruta para el html de descargar de Dynamo
@home_bp.route('/descargar_DynamoPage')
def descargar_DynamoPage():
    return render_template('descargarDynamo.html', archivo_generado=False)