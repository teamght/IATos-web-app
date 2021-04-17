from os import environ

ENDPOINT_TENSORFLOW_MODEL = environ.get('ENDPOINT_TENSORFLOW_MODEL')

# Base de datos
DB_URI = environ.get('MONGODB_URL')