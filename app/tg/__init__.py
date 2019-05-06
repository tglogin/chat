# tg
from flask import Blueprint

tg = Blueprint('tg', __name__)
from . import views
