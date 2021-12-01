import logging
from flask import Flask
from flask.templating import render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db=SQLAlchemy()

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)

    # Load the config file specified by the APP environment variable
    app.config.from_object(settings_module)
    # Load the configuration from the instance folder
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)
   
    # app.config['SECRET_KEY'] = 'ad69a0eda6e29ead949e440f0cd17101547ff07a'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gabospa:clave12345@localhost:5432/miniblog2'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Load the config for logging
    configure_logging(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    db.init_app(app)

    # Registro de Blueprints+
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_pb
    app.register_blueprint(public_pb)

    # Custom error handlers
    register_error_handlers(app)
    
    return app


def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404


def configure_logging(app):
    # Eliminamos los posibles manejadores del logger por defecto
    del app.logger.handlers[:]

    # Añadimos el logger por defecto a la lista de loggers
    # loggers = [app.logger, logging.getLogger('sqlalchemy') ]
    loggers = [app.logger,  ]
    handlers = []

    # Creamos un manejador para escribir los mensajes por consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(verbose_formatter())

    # Definimos confguracion para cada entorno
    if (app.config['APP_ENV'] == app.config['APP_ENV_LOCAL']) or (
        app.config['APP_ENV'] == app.config['APP_ENV_TESTING']) or (
        app.config['APP_ENV'] == app.config['APP_ENV_DEVELOPMENT']):
        console_handler.setLevel(logging.DEBUG)
        handlers.append(console_handler)
    elif app.config['APP_ENV'] == app.config['APP_ENV_PRODUCTION']:
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)

        mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                                    app.config['DONT_REPLY_FROM_EMAIL'],
                                    app.config['ADMINS'],
                                    '[Error][{}] La aplicación falló'.format(app.config['APP_ENV']),
                                    (app.config['MAIL_USERNAME'],
                                    app.config['MAIL_PASSWORD']), ()
        )
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(mail_handeler_formatter())
        handlers.append(mail_handler)

    # Asociamos cada uno de los handlers a cada uno de los loggers
    for log in loggers:
        for handler in handlers:
            log.addHandler(handler)
        log.propagate = False
        log.setLevel(logging.DEBUG)


def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )


def mail_handeler_formatter():
    return logging.Formatter(
        '''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s.%(msecs)d
            Message:
            %(message)s
        ''',
        datefmt='%d/%m/%Y %H:%M:%S'

    )