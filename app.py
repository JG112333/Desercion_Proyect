from flask import Flask
import logging
import os
from routes.home import home_bp
from routes.predict import predict_bp
from routes.csv_handler import csv_bp
from routes.xlsx_handler import xlsx_bp
from routes.traerS3_lista import traerS3r_bp
from routes.chatbot_handler import chatbot_bp
from routes.trans_xlsx_handler import trans_xlsx_bp
from routes.trans_csv_handler import trans_csv_bp
from routes.descargarDynamo_handler import descargarDynamo_bp


app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,  # Configura el nivel de los mensajes a capturar
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
    handlers=[
        logging.FileHandler('app.log'),  # Guardar los logs en un archivo llamado 'app.log'
        logging.StreamHandler()  # Mostrar los logs en la consola
    ]
)

# Configurar el logging de matplotlib para solo mostrar warnings y errores
logging.getLogger('matplotlib').setLevel(logging.WARNING)

# Registrar los Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(predict_bp)
app.register_blueprint(csv_bp)
app.register_blueprint(xlsx_bp)
app.register_blueprint(traerS3r_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(trans_xlsx_bp)
app.register_blueprint(trans_csv_bp)
app.register_blueprint(descargarDynamo_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))