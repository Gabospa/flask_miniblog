from .default import *

# Parameters to activate debug mode
TESTING = True
DEBUG = True

APP_ENV = APP_ENV_TESTING
SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'
