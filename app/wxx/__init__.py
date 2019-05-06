"""
王相新
"""
from flask import Blueprint

wxx = Blueprint('wxx', __name__)

from .views import *
