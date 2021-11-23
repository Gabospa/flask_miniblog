from flask import Blueprint

public_pb = Blueprint('public', __name__, template_folder='templates')

from .import routes