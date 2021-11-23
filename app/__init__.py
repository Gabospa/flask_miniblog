from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db=SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'ad69a0eda6e29ead949e440f0cd17101547ff07a'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gabospa:clave12345@localhost:5432/miniblog2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

    return app                                                   


