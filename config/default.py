
from os.path import abspath, dirname


# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = 'ad69a0eda6e29ead949e440f0cd17101547ff07a'

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuracion de email
MAIL_SERVER = 'tu servidor smtp'
MAIL_PORT = 587
MAIL_USERNAME = 'tu correo'
MAIL_PASSWORD = 'tu contraseña'
DONT_REPLY_FROM_EMAIL = 'direccion from'
ADMINS = ('gabospa@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False