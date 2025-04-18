# config.py
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
AWS_S3_BUCKET = os.getenv('AWS_S3_BUCKET')
AWS_DYNAMODB_TABLE = os.getenv('AWS_DYNAMODB_TABLE')